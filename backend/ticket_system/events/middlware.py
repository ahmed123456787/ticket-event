from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.middleware import BaseMiddleware
from urllib.parse import parse_qs
import jwt  

User = get_user_model()

class AuthenticationMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        close_old_connections()
        query_string = scope.get('query_string', b'').decode()
        query_params = parse_qs(query_string)
        token = query_params.get('token', [None])[0]

        if token:
            user = await self.get_user_from_jwt(token)
            scope['user'] = user if user else AnonymousUser()
        else:
            scope['user'] = AnonymousUser()  

        return await super().__call__(scope, receive, send)

    async def get_user_from_jwt(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get('user_id')
            if user_id:
                return await User.objects.aget(id=user_id)
        except jwt.ExpiredSignatureError:
            # Handle expired token
            return None
        except jwt.InvalidTokenError:
            # Return an instance of AnonymousUser instead of the class
            return AnonymousUser()
        return None