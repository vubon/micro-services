import requests

user_info_url = "http://localhost:8000/api/v1/user-validation/"
token_validation_url = "http://localhost:8000/api/v1/token-validation/"


class AuthService:

    @staticmethod
    def token_validation(token):
        """
        :param token:
        :return:
        """
        try:
            response = requests.post(token_validation_url, json=token)
            if 200 <= response.status_code <= 299:
                return response.json(), response.status_code
            elif 400 <= response.status_code <= 499:
                return response.json(), response.status_code

        except requests.exceptions.ConnectionError:
            message = {"error_msg": "Server error"}
            status_code = 500
            return message, status_code

    @staticmethod
    def user_info_collection(request_data):
        """
        :param request_data:
        :return:
        """
        data = {
            "user_token": request_data['user_token'],
            "rcv_phone": request_data['rcv_phone']
        }
        try:
            response = requests.post(user_info_url, json=data)

            if response.status_code == 200:
                return response.json(), response.status_code
            elif 400 <= response.status_code <= 499:
                return response.json(), response.status_code

        except requests.exceptions.ConnectionError:
            message = {"error_msg": "Server error"}
            status_code = 500
            return message, status_code

