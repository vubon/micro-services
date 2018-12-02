import logging

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer

# token_decode = api_settings.JWT_DECODE_HANDLER
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
            res = self.serializer.validate(token)
        except Exception as e:
            # logger.debug('Internal get user refresh token {}'.format(e))
            return False

        if 'token' in res.keys():
            new_token = res['token']
            final_token = encode_handler(new_token)
            return final_token

        return False
