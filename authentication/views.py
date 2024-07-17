from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .utils import generate_jwt, decode_jwt
from functools import wraps
import json

def jwt_required(func):
    @wraps(func)
    def wrapper_function(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if token:
            token = token.split(' ')[1]
            payload = decode_jwt(token)
            if payload:
                return func(request, *args, **kwargs)
        return JsonResponse({'error': 'Unauthorized'}, status=401)

    return wrapper_function

@jwt_required
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['username'] and data['password']:
            print(data);
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                print(f"user : {user}")
                return JsonResponse({'message' : 'login success', 'status':200})
    return HttpResponse('bad http request')

def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if data['username'] and data['fullname'] and data['email'] and data['password']:
            user = CustomUser.objects.create_user(username=data['username'], 
                                                full_name=data['fullname'], 
                                                email=data['email'], 
                                                password=data['password'])
            if user is not None:
                token = generate_jwt(user)
                return JsonResponse({'message' : 'user registred succefully', 'status':200, 'token':token})
    return HttpResponse('bad http request')

@jwt_required
def changePassword(request):
    if request.method == 'POST':
        print(f"request user : {request.user}")
        if request.user.is_authenticated:
            print(f"request user : {request.user}")
        return HttpResponse('done')
    return HttpResponse('bad http request')
