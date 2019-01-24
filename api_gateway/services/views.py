from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from services.decarators import valid_url_for_gateway


class APIGatewayPostMethod(APIView):
    """
        URL: /api/v1/
    """
    @method_decorator(valid_url_for_gateway)
    def get(self, request, *args, **kwargs):
        print(request.META.get("PATH_INFO"))

        return Response("Test", status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        return Response("Test Post", status=status.HTTP_201_CREATED)
