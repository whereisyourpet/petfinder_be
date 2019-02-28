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
            auth.login(request, user)
            return JsonResponse({
                'success': 1,
                'msg': "登陆成功"
            })
        else:
            return JsonResponse({
                'success': 0,
                'msg': "用户名或密码错误"
            })
    else:
        return JsonResponse({
            'success': 0,
            'msg': 'Wrong method'
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
                'msg': '用户名重复'
            })
        else:
            User.objects.create_user(
                username=username, password=password, nickname=nickname)
            return JsonResponse({
                'success': 1,
                'msg': '注册成功'
            })
    else:
        return JsonResponse({
            'success': 0,
            'msg': 'Wrong method'
        })


def accounts_logout(request):
    """
    The logout api
    """
    auth.logout(request)
    return JsonResponse({
        'success': 1
    })


def status(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'status': 1,
            'username': request.user.get_username()
        })
    else:
        return JsonResponse({
            'status': 0
        })
