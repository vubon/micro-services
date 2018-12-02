from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fnf.models import FamilyMember
from friends_and_family.decarators import token_validation


class AddFamilyMemberView(APIView):
    """
        URL: /api/v1/add-family-member/
        POST: POST
        {
            "rcv_phone": "mobile number"
        }
    """
    @method_decorator(token_validation)
    def post(self, request, *args, **kwargs):
        request.data['user_token'] = request.META.get("HTTP_AUTHORIZATION")
        response, status_code = FamilyMember.objects.create_member(request.data)

        return Response(response, status=status_code)


class FamilyMemberList(APIView):
    """
        URL: /api/v1/family-member/
    """

    @method_decorator(token_validation)
    def get(self, request, *args, **kwargs):
        request.data['phone_number'] = kwargs['user_data']['phone_number']
        response = FamilyMember.objects.family_member_list(request.data)
        return Response(response, status=status.HTTP_200_OK)

