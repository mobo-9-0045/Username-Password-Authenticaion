import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.core.signing import Signer
from .models import CustomUser

def checkUserPayload(payload):
    user = CustomUser.objects.get(username=payload['username']);
    if user is not None:
        if user.id == payload['id'] and user.password == payload['password']:
            return 200
    return 401

def generate_jwt(user):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=4),
        'iat': datetime.utcnow(),
        'username':user.username,
        'id': user.id,
        'password': user.password,
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None