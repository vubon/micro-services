from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from fnf.models import FamilyMember


class AddFamilyMemberView(APIView):
    """
        URL: /api/v1/add-family-member/
        POST: POST
    """

    def post(self, request, *args, **kwargs):
        user_token = request.META.get("HTTP_AUTHORIZATION")
        if not user_token:
            return Response({"error_msg": "Invalid"}, status=status.HTTP_400_BAD_REQUEST)

        request.datap['token'] = user_token
        response, status_code = FamilyMember.objects.create_member(request.data)

        return Response(response, status=status_code)
