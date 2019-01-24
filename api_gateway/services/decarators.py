import json

from django.http import HttpResponseBadRequest, HttpResponseServerError, HttpResponse

from applibs.auth_service import AuthService

auth = AuthService()


def token_validation(func):
    """
    :param func:
    :return:
    """

    def wrapper(request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        if "HTTP_AUTHORIZATION" not in request.META:
            return HttpResponseBadRequest(json.dumps({"error_msg": "You have no permission"}))

        token = request.META.get("HTTP_AUTHORIZATION")

        if not token:
            return HttpResponseBadRequest(json.dumps({"error_msg": "No Token"}))

        res, status_code = auth.token_validation({"user_token": token})

        if 500 <= status_code <= 599:
            return HttpResponseServerError(json.dumps(res))

        if 400 <= status_code <= 499:
            return HttpResponseBadRequest(json.dumps(res))

        if 200 <= status_code <= 299:
            kwargs['user_data'] = res
            kwargs['status_code'] = status_code

        return func(request, *args, **kwargs)

    return wrapper


def valid_url_for_gateway(func):
    """
    :param func:
    :return:
    """

    def wrapper(request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        request_path = request.META.get("PATH_INFO")
        url = request_path.split('/')
        api = url[1]
        version = url[2]
        print(api, version)

        return func(request, *args, **kwargs)

    return wrapper
