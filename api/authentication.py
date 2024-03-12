import jwt
from .models import UserDetails
from django.conf import settings
# might need this for ClientUser auth later
# from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


# Custom JWT token auth class
class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Extract JWT token from request headers
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            raise AuthenticationFailed('Authentication header missing')

        try:
            # Split the auth header and extract the token
            token = auth_header.split()[1]
            # Decode and verify the token using the secret key
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # Retrieve the user_id from the token payload
            user_id = payload['user_id']
            # Fetch the user object using the user_id
            user = UserDetails.objects.get(pk=user_id)

            # Setting request user field
            # Note: this needs to be done to identify the user
            request.user = user
            # Return the user and token
            return (user, token)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        except UserDetails.DoesNotExist:
            raise AuthenticationFailed('User not found')