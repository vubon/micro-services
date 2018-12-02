from django.db import models
from django.db.models import F
from django.utils import timezone

from applibs.auth_service import AuthService

auth = AuthService()


class FamilyMemberManager(models.Manager):

    def create_member(self, request_data: dict) -> tuple:
        """
        :param request_data:
        :return:
        """
        res, status_code = auth.user_info_collection(request_data)

        if 500 <= status_code <= 599:
            return res, status_code

        if 400 <= status_code <= 499:
            return res, status_code

        filter_data = self.filter(request_made_by=res['sender_phone'], request_sent_to=res['rcv_phone'])

        if filter_data.exists():
            message = {"error_msg": "Relation already exists"}
            status_code = 400
            return message, status_code

        self.create(
            request_made_by=res['sender_phone'],
            request_sent_to=res['rcv_phone'],
            sender_full_name=res['sender_name'],
            receiver_full_name=res['rcv_name'],
            created_at=timezone.now()
        )
        message = {"success": "Success"}
        status_code = 201
        return message, status_code

    def family_member_list(self, request_data: dict) -> tuple:
        """
        :param request_data:
        :return:
        """
        # res, status_code = auth.token_validation(request_data)
        #
        # if 500 <= status_code <= 599:
        #     return res, status_code
        #
        # if 400 <= status_code <= 499:
        #     return res, status_code

        return self.filter(
            request_made_by=request_data['phone_number']
        ).annotate(
            rcv_phone=F('request_sent_to'),
            rcv_name=F('receiver_full_name'),
        ).values(
            'rcv_phone', 'rcv_name', 'created_at', 'is_active'
        )


class FamilyMember(models.Model):
    request_made_by = models.CharField(max_length=15, db_index=True)
    request_sent_to = models.CharField(max_length=15, db_index=True)
    sender_full_name = models.CharField(max_length=256)
    receiver_full_name = models.CharField(max_length=256)

    created_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    objects = FamilyMemberManager()

    def __str__(self):
        return "{} to {}".format(self.request_made_by, self.request_sent_to)
