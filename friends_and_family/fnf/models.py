from django.db import models

from applibs.auth_service import AuthService

auth = AuthService()


class FamilyMemberManager(models.Manager):

    def create_member(self, request_data: dict) -> tuple:
        """
        :param request_data:
        :return:
        """
        res = auth.user_info_collection(request_data)
        self.create(
            request_made_by=res['sender_phone'],
            request_sent_to=res['rcv_phone'],
            sender_full_name=res['sender_name'],
            receiver_full_name=res['rcv_name']
        )
        message = {"success": "Success"}
        status_code = 201
        return message, status_code


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
