import logging

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer

token_decode = api_settings.JWT_DECODE_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# # Get an instance of a logger
# logger = logging.getLogger('general')


class RefreshToken:
    serializer = RefreshJSONWebTokenSerializer()

    def token_validation(self, token):
        """
        :param token:
        :return:
        """
        try:
            res = self.serializer.validate({"token": token['token'].split(' ')[1]})
        except Exception as e:
            print(e)
            # logger.debug('Internal get user refresh token {}'.format(e))
            return False

        if 'token' in res.keys():
            return res['token']

        return False
