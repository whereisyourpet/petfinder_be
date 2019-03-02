from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import pet_info
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
        # 通过用户id筛选该用户所发布的流浪动物信息，并返回
        # 这里只是示范

        username = request.user.get_username()              # 获取用户唯一辨识符--用户名
        # pets = User.objects.filter(username=username)     # 根据用户名筛选符合要求的流浪动物信息
        return JsonResponse({
            'success':           1,
            'pet_name':         '二哈',
            'pet_type':         '汪汪汪',
            'pet_gender':       '公',
            'pet_age':           1,
            'primary_breed':    'Akita',
            'secondary_breed':  'Boxer',
            'primary_color':    '黑色',
            'secondary_color1': '灰色',
            'secondary_color2': '白色',
            'maturity_size':    '九米级究极巨人',
            'fur_length':       '短毛',
            '成年体长':          '25',
            'state':            'Johor',
            'dewormed':         '是',
            'sterilized':       '有',
        })
        # return JsonResponse({
        #     'success':           1,
        #     'pet_name':         pets.pet_name,
        #     'pet_type':         pets.pet_type,
        #     'pet_gender':       pets.gender,
        #     'pet_age':          pets.pet_age,
        #     'primary_breed':    pets.primary_breed,
        #     'secondary_breed':  pets.secondary_breed,
        #     'primary_color':    pets.primary_color,
        #     'secondary_color1': pets.secondary_color1,
        #     'secondary_color2': pets.secondary_color2,
        #     'maturity_size':    pets.maturity_size,
        #     'fur_length':       pets.fur_length,
        #     #'成年体长':          unknow data
        #     'state':            pets.state,
        #     'dewormed':         pets.dewormed,
        #     'sterilized':       pets.sterilized,
        # })
    else:
        return JsonResponse({
            'success':           0,
        })


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
        #length          = request.POST['length']

        pets.create_pet(
            publisher_name  = publisher_name,
            pet_name        = pet_name,
            pet_type        = pet_type,
            pet_gender      = pet_gender,
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
            sterilized      = sterilized,)
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
