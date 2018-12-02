import requests

user_info_url = "http://localhost:8000/api/v1/user-validation/"


class AuthService:

    @staticmethod
    def token_validation(token):
        """
        :param token:
        :return:
        """
        data = {
            "token": token
        }
        response = requests.post('', json=data)
        if response.status_code == 200:
            return True
        return False

    @staticmethod
    def user_info_collection(request_data):
        """
        :param request_data:
        :return:
        """
        data = {
            "user_token": request_data['token'],
            "rcv_phone": request_data['rcv_phone']
        }
        response = requests.post(user_info_url, json=data)

        if response.status_code == 200:
            return response.json()
        return False
