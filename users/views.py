from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User

# Create your views here.


@csrf_exempt
def accounts_login(request):
    """
    The login api
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return JsonResponse({
                'success': 1
            })
        else:
            return JsonResponse({
                'success': 0,
                'msg': "failed"
            })
    else:
        return JsonResponse({
            'success': 0
        })


@csrf_exempt
def accounts_register(request):
    """
    The register api
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        nickname = request.POST['nickname']

        user = User.objects.filter(username=username)
        if user.exists():
            return JsonResponse({
                'success': 0,
                'msg': 'repeated'
            })
        else:
            User.objects.create_user(
                username=username, password=password, nickname=nickname)
            return JsonResponse({
                'success': 1,
                'msg': 'ojbk'
            })
    else:
        return JsonResponse({
            'success': 0,
            'msg': 'Wrong method'
        })
