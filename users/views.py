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
    """
    Get current session information
    """
    if request.user.is_authenticated:
        return JsonResponse({
            'status': 1,
            'username': request.user.get_username()
        })
    else:
        return JsonResponse({
            'status': 0
        })


@csrf_exempt
def accounts_modify(request):
    """
    Modify user information
    """
    if request.user.is_authenticated and request.method == "POST":

        user = request.user

        if "email" in request.POST:
            user.email = request.POST["email"]

        if "location" in request.POST:
            user.location = request.POST["location"]

        if "nickname" in request.POST:
            user.nickname = request.POST["nickname"]

        if "has_pet" in request.POST:
            user.has_pet = request.POST["has_pet"]

        if "willing" in request.POST:
            user.willing = request.POST["willing"]

        if "number" in request.POST:
            user.number = request.POST["number"]

        if "married" in request.POST:
            user.married = request.POST["married"]

        if "phone" in request.POST:
            user.phone = request.POST["phone"]

        if "gender" in request.POST:
            user.gender = request.POST["gender"]

        if "description" in request.POST:
            user.description = request.POST["description"]

        user.save()
        return JsonResponse({
            'success': 1,
            'msg': "信息修改成功"
        })

    else:
        return JsonResponse({
            'success': 0,
            'msg': "信息修改失败"
        })


def get_user_info(request):
    """
    Get all user information
    """
    if request.user.is_authenticated:
        return JsonResponse({
            'success': 1,
            'username': request.user.get_username(),
            'email': request.user.email,
            'nickname': request.user.nickname,
            'location': request.user.location,
            'has_pet': request.user.has_pet,
            'willing': request.user.willing,
            'number': request.user.number,
            'phone': request.user.phone,
            'married': request.user.married,
            'gender': request.user.gender,
            'description': request.user.description,
        })
    else:
        return JsonResponse({
            'success': 0
        })
