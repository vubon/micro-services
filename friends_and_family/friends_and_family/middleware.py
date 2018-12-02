import json
from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin

from applibs.auth_service import AuthService

auth = AuthService()


class TokenValidationTwo(MiddlewareMixin):
    def process_request(self, request):
        if "HTTP_AUTHORIZATION" not in request.META:
            return HttpResponseBadRequest("You have no permission")

    def process_response(self, request, response):
        token = request.META.get('HTTP_AUTHORIZATION', None)

        if not token:
            return HttpResponseBadRequest(json.dumps({"error_msg": "Invalid Token"}))

        res, status_code = auth.token_validation({"user_token": token})

        if 500 <= status_code <= 599:
            response['error_msg'] = res
            response['status_code'] = status_code

        if 400 <= status_code <= 499:
            response['error_msg'] = res
            response['status_code'] = status_code

        return response


class TokenValidation:
    """
        Token Validation Middleware
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if "HTTP_AUTHORIZATION" not in request.META:
            return HttpResponseBadRequest(json.dumps({"error_msg": "You have no permission"}))

        response = self.get_response(request)

        token = request.META.get('HTTP_AUTHORIZATION', None)

        if not token:
            return HttpResponseBadRequest(json.dumps({"error_msg": "Invalid Token"}))

        res, status_code = auth.token_validation({"user_token": token})

        if 500 <= status_code <= 599:
            response['error_msg'] = res
            response['status_code'] = status_code

        if 400 <= status_code <= 499:
            response['error_msg'] = res
            response['status_code'] = status_code

        return response
