from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings

from .utils import RefreshToken

refresh_token = RefreshToken()

token_decode = api_settings.JWT_DECODE_HANDLER


class SignUpView(APIView):
    """
        URL: /api/v1/sign-up/
        Method: POST
    """
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.create(username=request.data['username'], first_name=request.data['first_name'],
                                       last_name=request.data['last_name'])
            user.set_password(request.data['password'])
            user.save()
            return Response({"msg": "Success"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"error_msg": "Failed"}, status=status.HTTP_400_BAD_REQUEST)


class TokenValidation(APIView):
    """
        URL: /api/v1/token-validation/
    """

    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        new_token = refresh_token.token_validation({"token": request.data['user_token']})

        if not new_token:
            return Response({"error_msg": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)

        # decode new token
        decoded_token = token_decode(new_token)
        user_obj = User.objects.get(username=decoded_token['username'])
        data = dict()

        data['name'] = user_obj.get_full_name()
        data['phone_number'] = user_obj.username

        return Response(data, status=status.HTTP_200_OK)


class UserValidation(APIView):
    """
        URL: /api/v1/user-validation/
        Method: POST

        {
            "user_token": "token',
            "rcv_phone": "mobile number"
        }
    """
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        new_token = refresh_token.token_validation({"token": request.data['user_token']})

        if not new_token:
            return Response("Invalid Token", status=status.HTTP_400_BAD_REQUEST)

        # decode new token
        decoded_token = token_decode(new_token)
        sender_obj = User.objects.get(username=decoded_token['username'])
        rcv_obj = User.objects.filter(username=request.data['rcv_phone'])

        if not rcv_obj.exists():
            return Response({"error_msg": "Invalid Receiver user"}, status=status.HTTP_400_BAD_REQUEST)

        data = dict()

        data['sender_name'] = sender_obj.get_full_name()
        data['sender_phone'] = sender_obj.username
        data['rcv_name'] = rcv_obj[0].get_full_name()
        data['rcv_phone'] = rcv_obj[0].username

        return Response(data, status=status.HTTP_200_OK)
