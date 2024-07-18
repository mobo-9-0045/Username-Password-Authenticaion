from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .utils import generate_jwt, decode_jwt, checkUserPayload
from functools import wraps
import json

def jwt_required(func):
    @wraps(func)
    def wrapper_function(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            payload = decode_jwt(token)
            if payload:
                if checkUserPayload(payload) == 200:
                    request.user = payload
                    return func(request, *args, **kwargs)
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    return wrapper_function

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['username'] and data['password']:
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                token = generate_jwt(user)
                return JsonResponse({'message': 'login success', 'token': token}, status= 200)
            return JsonResponse({'error': 'bad credential',}, status=401)
    return HttpResponse('bad http request')

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if (data['username'] and 
            data['fullname'] and 
            data['email'] and 
            data['password']):
            user = CustomUser.objects.create_user(username=data['username'], 
                                                    full_name=data['fullname'], 
                                                    email=data['email'], 
                                                    password=data['password'])
            if user is not None:
                return JsonResponse({'message' : 'user registred succefully'}, status=200)
        return HttpResponse('somthin went wrong');
    return HttpResponse('bad http request')

@jwt_required
def changePassword(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['newpassword']:
            user = CustomUser.objects.get(id=request.user['id'])
            if user is not None:
                print(f"new password : {data['newpassword']}")
                user.set_password(data['newpassword'])
                user.save()
        return HttpResponse(status=200)
    return HttpResponse('bad http request')

@jwt_required
def updateInfo(request):
    pass
