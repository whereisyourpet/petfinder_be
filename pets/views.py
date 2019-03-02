from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import pet_info
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.
def get_pet_info(request):
    """
    Get all pet's information
    用户点击数据展示调用该接口，返回显示数据
    """
    ##
    # 需要用户登陆后才能进行观看
    # 否则返回空
    ##
    if request.user.is_authenticated:
        username = request.user.get_username()                        # 获取用户唯一辨识符--用户名
        pets = pet_info.objects.filter(publisher_name=username)       # 根据用户名筛选符合要求的流浪动物信息
        data = serializers.serialize("json",pets)
        # return JsonResponse(data, safe=False)
        return JsonResponse({
            'success':           1,
            'data':             data,
        })
    else:
        return JsonResponse({
            'success':           0,
        })


@csrf_exempt
def publish_pet_information(request):
    """
    Publish new stray animails
    用户在助宠寻主上发布新流浪动物信息，调用该接口新建动物信息词条
    """
    ###
    ## 用户只有在登录后才能发布流浪动物的信息
    ###
    if request.user.is_authenticated and request.method == "POST":
        # 提取json信息
        # 判断是否空，若空则为，默认值
        # 由前端判断
        publisher_name  = request.user.get_username()
        pet_name        = request.POST['pet_name']
        pet_type        = request.POST['pet_type']
        pet_gender      = request.POST['pet_gender']
        pet_age         = request.POST['pet_age']
        primary_breed   = request.POST['primary_breed']
        secondary_breed = request.POST['secondary_breed']
        primary_color   = request.POST['primary_color']
        secondary_color1= request.POST['secondary_color1']
        secondary_color2= request.POST['secondary_color2']
        maturity_size   = request.POST['maturity_size']
        fur_length      = request.POST['fur_length']
        state           = request.POST['state']
        dewormed        = request.POST['dewormed']
        sterilized      = request.POST['sterilized']
        vaccinated      = request.POST['vaccinated']
        health          = request.POST['health']
        quantity        = request.POST['quantity']
        fee             = request.POST['fee']
        video_amt       = request.POST['video_amt']
        photo_amt       = request.POST['photo_amt']
        description     = request.POST['description']
        #length          = request.POST['length']

        print("\n")
        print(request.POST)
        print("\n")

        pet_info.objects.create(
            rescuer_name    = 'None',
            publisher_name  = publisher_name,
            pet_name        = pet_name,
            pet_type        = pet_type,
            gender          = pet_gender,
            pet_age         = pet_age,
            primary_breed   = primary_breed,
            secondary_breed = secondary_breed,
            primary_color   = primary_color,
            secondary_color1= secondary_color1,
            secondary_color2= secondary_color2,
            maturity_size   = maturity_size,
            fur_length      = fur_length,
            state           = state,
            dewormed        = dewormed,
            sterilized      = sterilized,
            vaccinated      = vaccinated,
            health          = health,
            quantity        = quantity,
            fee             = fee,
            video_amt       = video_amt,
            photo_amt       = photo_amt,
            description     = description,)
        return JsonResponse({
            'success': 1,
            'msg': '发布成功'
        })
    else:
        return JsonResponse({
            'success': 0,
            'msg': 'Wrong method'
        })

def recommand_pets(request):
    """
    Recommand pets to users
    用户在猜你喜欢上输入期望参数，调用该接口返回推荐的宠物信息
    """
    pass
