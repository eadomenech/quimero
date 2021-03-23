from flask_login import UserMixin
import jwt


class User(UserMixin):
    """Standard flask_login UserMixin"""
    id = ''
    username = ''
    email = ''

    def __init__(self, id='', username='', email=''):
        self.id = id
        self.username = username
        self.email = email


class TokenDecode:
    
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token - :param auth_token: - :return: integer|string
        """
        try:
            public_key = open('private/jwt-key.pub').read()
            payload = jwt.decode(
                auth_token, public_key, algorithms=['RS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'