import json

from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin

PRE_DEFINED_HTTP_VERBS = ['GET', 'POST', 'DELETE']


class ParseURL(MiddlewareMixin):

    def process_request(self, request):
        request_path = request.META.get("PATH_INFO")
        url = request_path.split('/')
        api = url[1]
        version = url[2]
        service_name = url[3]
        task_path = url[4]
        print(api, version, service_name, task_path)
        request_method = request.META.get("REQUEST_METHOD")
        if request_method not in PRE_DEFINED_HTTP_VERBS:
            return HttpResponseBadRequest("Invalid request")
        return api + "/" + version + "/"

