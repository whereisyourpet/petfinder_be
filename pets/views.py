from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .models import pet,state
from .models import state as STATEOBJECT
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from numpy import *
import numpy as np
import operator
import csv

import json
import uuid

# Create your views here.
def get_pets_of_user(request):
    """
    用户登陆后才可调用该请求，返回该用户已发布的宠物id列表
    """
    ##
    # 需要用户登陆后才能进行观看
    # 否则返回空
    ##
    if request.user.is_authenticated:
        username = request.user.get_username()                        # 获取用户唯一辨识符--用户名
        data = list(pet.objects.filter(publisher_name=username).values('pet_id')) # 根据用户名筛选符合要求的流浪动物信息
        # return JsonResponse(data, safe=False)
        return JsonResponse({
            'success':           1,
            'data':             data,
        })
    else:
        return JsonResponse({
            'success':           0,
        })

def setdefault(tmpstr):
    if(len(tmpstr)==0):
        return 0
    else:
        return int(tmpstr)

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
        pet_id          = str(uuid.uuid1()).replace("-","")
        publisher_name  = request.user.get_username()
        pet_name        = request.POST['pet_name']
        pet_type        = setdefault(request.POST['pet_type'])
        pet_gender      = setdefault(request.POST['pet_gender'])
        pet_age         = setdefault(request.POST['pet_age'])
        primary_breed   = setdefault(request.POST['primary_breed'])
        secondary_breed = setdefault(request.POST['secondary_breed'])
        primary_color   = setdefault(request.POST['primary_color'])
        secondary_color1= setdefault(request.POST['secondary_color1'])
        secondary_color2= setdefault(request.POST['secondary_color2'])
        maturity_size   = setdefault(request.POST['maturity_size'])
        fur_length      = setdefault(request.POST['fur_length'])
        receive_state_id= request.POST['state']
        dewormed        = setdefault(request.POST['dewormed'])
        sterilized      = setdefault(request.POST['sterilized'])
        vaccinated      = setdefault(request.POST['vaccinated'])
        health          = setdefault(request.POST['health'])
        quantity        = setdefault(request.POST['quantity'])
        fee             = setdefault(request.POST['fee'])
        video_amt       = setdefault(request.POST['video_amt'])
        photo_amt       = setdefault(request.POST['photo_amt'])
        description     = request.POST['description']

        # 设置默认值

        if(len(receive_state_id)!=0):
            print(111)
            state = STATEOBJECT.objects.filter(state_id=int(receive_state_id))
        else:
            print(222)
            state = STATEOBJECT.objects.filter(state_id=1)
        print(state)
        pet.objects.create(
            rescuer_name    = 'None',
            pet_id          = pet_id,
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
            state           = state[0],
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

@csrf_exempt
def modify(request):
    """
    Modify pet information
    """
    if request.user.is_authenticated and request.method == "POST":
        pet = models.pet.objects.get(pet_id=request.POST["pet_id"])

        if "pet_name" in request.POST:
            pet.pet_name = request.POST["pet_name"]

        if "pet_type" in request.POST:
            pet.pet_type = request.POST["pet_type"]

        if "pet_gender" in request.POST:
            pet.pet_gender = request.POST["pet_gender"]

        if "pet_age" in request.POST:
            pet.pet_age = request.POST["pet_age"]

        if "primary_breed" in request.POST:
            pet.primary_breed = request.POST["primary_breed"]

        if "secondary_breed" in request.POST:
            pet.secondary_breed = request.POST["secondary_breed"]

        if "primary_color" in request.POST:
            pet.primary_color = request.POST["primary_color"]

        if "secondary_color1" in request.POST:
            pet.secondary_color1 = request.POST["secondary_color1"]

        if "secondary_color2" in request.POST:
            pet.secondary_color2 = request.POST["secondary_color2"]

        if "maturity_size" in request.POST:
            pet.maturity_size = request.POST["maturity_size"]
            
        if "state" in request.POST:
            pet.state = request.POST["state"]

        if "fur_length" in request.POST:
            pet.fur_length = request.POST["fur_length"]

        if "dewormed" in request.POST:
            pet.dewormed = request.POST["dewormed"]   

        if "sterilized" in request.POST:
            pet.sterilized = request.POST["sterilized"]   

        pet.save()
        return JsonResponse({
            'success': 1,
            'msg': "信息修改成功"
        })

    else:
        return JsonResponse({
            'success': 0,
            'msg': "信息修改失败"
        })

def delete(request):
    """
    delete  pet information
    """
    if request.user.is_authenticated and request.method == "POST":
        pet = models.pet.objects.filter(pet_id=request.POST["pet_id"]).delete()
        return JsonResponse({
            'success': 1,
            'msg': "信息删除成功"
        })

    else:
        return JsonResponse({
            'success': 0,
            'msg': "信息删除失败"
        })  

# 用户输入喜爱动物的参数，函数返回推荐宠物
@csrf_exempt
def get_recommand_pets(request):
    """
    Recommand pets to users
    用户在猜你喜欢上输入期望参数，调用该接口返回推荐的宠物信息
    """
    """
    用户可以输入的参数有
    领养费用    类别        性别       年龄
    主要血统    次要血统    主要毛色    次要毛色1&2
    体型        毛长       所在州      是否绝育
    是否除虫    有无疫苗    健康程度

    返回k只推荐的宠物，调用时需指明k
    返回的信息有
    动物id      动物名称    易收养指数  受欢迎程度
    """
    if request.user.is_authenticated and request.method == "POST":
        publisher_name  = request.user.get_username()
        pet_type,w_pet_type       = str_to_int(request.POST['pet_type'])
        pet_gender,w_pet_gender      = str_to_int(request.POST['pet_gender'])
        pet_age,w_pet_age         = str_to_int(request.POST['pet_age'])
        primary_breed,w_primary_breed   = str_to_int(request.POST['primary_breed'])
        secondary_breed,w_secondary_breed = str_to_int(request.POST['secondary_breed'])
        primary_color,w_primary_color   = str_to_int(request.POST['primary_color'])
        secondary_color1,w_secondary_color1= str_to_int(request.POST['secondary_color1'])
        secondary_color2,w_secondary_color2= str_to_int(request.POST['secondary_color2'])
        maturity_size,w_maturity_size   = str_to_int(request.POST['maturity_size'])
        fur_length,w_fur_length      = str_to_int(request.POST['fur_length'])
        state,w_state           = str_to_int(request.POST['state'])
        dewormed,w_dewormed        = str_to_int(request.POST['dewormed'])
        sterilized,w_sterilized      = str_to_int(request.POST['sterilized'])
        vaccinated,w_vaccinated     = str_to_int(request.POST['vaccinated'])
        fee,w_fee             = str_to_int(request.POST['fee'])
        health,w_health          = str_to_int(request.POST['health'])
        k,w_k               = str_to_int(request.POST['k'])

        oralData = array(pet.objects.values_list(                                   # 获取数据库数据
            'pet_id','pet_type','pet_age','primary_breed','secondary_breed','gender',
            'primary_color','secondary_color1','secondary_color2','maturity_size',
            'fur_length','vaccinated','dewormed','sterilized','fee','state','health'))
        labels = oralData[:,0]                                                      # 获取宠物id作为labels
        dataset= oralData[:,1:]                                                     # 其余项作为数据集
        userinput = [                                                               # 获取用户数据数据
            pet_type,pet_age,primary_breed,secondary_breed,pet_gender,
            primary_color,secondary_color1,secondary_color2,maturity_size,
            fur_length,vaccinated,dewormed,sterilized,fee,state,health]
        #userinput = [2,4,300,0,2,2,1,0,1,1,3,1,1,20,41326,3]

        if(w_k==0):
            k = 5                                                                   # 设定需要推荐的宠物数量
        # 加权常数项
        # Type*10	Age*2	Breed1,2*2	Gender*10	Color1,2,3*2	MaturitySize*2	
        # FurLength*2	Vaccinated*10	Dewormed*10	Sterilized*10   Fee*2	State*1 health*10
        # dataweight = mat([10,2,2,2,10,2,2,2,2,2,10,10,10,2,1,10])
        dataweight = mat(
            [10*w_pet_type,         2*w_pet_age,            2*w_primary_breed,
            2*w_secondary_breed,    10*w_pet_gender,        2*w_primary_color,
            2*w_secondary_color1,   2*w_secondary_color2,   2*w_maturity_size,
            2*w_fur_length,         10*w_vaccinated,        10*w_dewormed,
            10*w_sterilized,        2*w_fee,                1*w_state,          10*w_health])
        if k>dataset.shape[0]:                                                      # 获取推荐的宠物的id
            pets_ID_list = list(labels)                                             
        else:
            pets_ID_list = recommand(userinput,dataset,labels,k,dataweight)

        resultdata=[]                                                               # 通过id获取需要返回的宠物id，宠物名字，易收养程度，受欢迎程度
        for i in pets_ID_list:
            resultdata.append(list(pet.objects.filter(pet_id=i).values(
                    'pet_id','pet_name','adoption_star','popularity_star')))
        return JsonResponse({                                                       # 返回结果
            'success':           1,
            'data':              resultdata,
        })
    else:
        return JsonResponse({
            'success': 0,
            'data': ''
        })

def str_to_int(tmpstr):
    if(len(tmpstr)==0):
        tmpstr = int(1)
        notempty = 0
    else:
        tmpstr = int(tmpstr)
        notempty = 1
    return tmpstr,notempty

# 算法实现
# 函数将返回距离inX加权欧式距离最近的k个数据项作为推荐值
def recommand(inX, dataSet, labels, k, dataweight):
    # 数据类型转化，转化成mat矩阵后进行一些线性操作
    inX=mat(inX)
    dataSet=mat(matrix_str_to_int(dataSet))
    labels=np.array(labels)

    # distances = (Σ(inX-dataSet(i))^2.*dataweight)^0.5
    dataSetSize = dataSet.shape[0]                  # 获取数据规模，即获取该数据矩阵有多少行
    diffMat = tile(inX, (dataSetSize,1))-dataSet    # tile(A,(m,n))  将数组A作为元素构造出m行n列的数组  X-Xi
    sqDiffMat = array(diffMat)**2                   # sqDiffMat = diffMat^2                          (X-Xi)^2
    
    dataweight = tile(dataweight,(dataSetSize,1))
    weightedsqDiffMat = np.multiply(sqDiffMat,dataweight)

    sqDistances = weightedsqDiffMat.sum(axis=1)     # array.sum(axis=1)按行累加，axis=0为按列累加      Σ(X-Xi)^2
    distances = array(sqDistances)**0.5             # distances = sqDistances^0.5                    
    sortedDistIndicies = distances.T.argsort().T    # array.argsort()，得到每个元素的排序序号
    
    recommandResult = []
    for i in range(k):
        recommandResult.append(labels[sortedDistIndicies[i][0]])
    return recommandResult

def matrix_str_to_int(tmpmatrix):
    width = tmpmatrix.shape[0]
    height = tmpmatrix.shape[1]
    newmatrix = np.zeros((width,height))

    for a in range(width):
        for b in range(height):
            newmatrix[a,b] = int(tmpmatrix[a,b])

    return newmatrix

@csrf_exempt
def petfilter(request):
    if request.user.is_authenticated and request.method == "POST":
        pet_type        = int(request.POST['pet_type'])
        pet_gender      = int(request.POST['pet_gender'])
        primary_color   = int(request.POST['primary_color'])
        secondary_color1= setdefault(request.POST['secondary_color1'])
        secondary_color2= setdefault(request.POST['secondary_color2'])
        state           = int(request.POST['state'])
        upfee           = int(request.POST['upfee'])
        downfee         = int(request.POST['downfee'])
        upquantity      = int(request.POST['upquantity'])
        downquantity    = int(request.POST['downquantity'])

        if(secondary_color1==0 and secondary_color2!=0):
            pets = pet.objects.filter(
                pet_type=pet_type,gender=pet_gender,primary_color=primary_color,
                secondary_color1=secondary_color2,
                state__state_id=state,fee__gte=downfee,fee__lt=upfee,
                quantity__gte=downquantity,quantity__lt=upquantity).values('pet_id')
        elif(secondary_color1!=0 and secondary_color2==0):
            pets = pet.objects.filter(
                pet_type=pet_type,gender=pet_gender,primary_color=primary_color,
                secondary_color1=secondary_color1,
                state__state_id=state,fee__gte=downfee,fee__lt=upfee,
                quantity__gte=downquantity,quantity__lt=upquantity).values('pet_id')
        elif(secondary_color1==0 and secondary_color2==0):
            pets = pet.objects.filter(
                pet_type=pet_type,gender=pet_gender,primary_color=primary_color,
                state__state_id=state,fee__gte=downfee,fee__lt=upfee,
                quantity__gte=downquantity,quantity__lt=upquantity).values('pet_id')
        else:
            pets = pet.objects.filter(
                pet_type=pet_type,gender=pet_gender,primary_color=primary_color,
                secondary_color1=secondary_color1,secondary_color2=secondary_color2,
                state__state_id=state,fee__gte=downfee,fee__lt=upfee,
                quantity__gte=downquantity,quantity__lt=upquantity).values('pet_id')
        data = serializers.serialize("json",pets)

        return JsonResponse({                                                       # 返回结果
            'success':           1,
            'data':              data,
        })
    else:
        return JsonResponse({
            'success': 0,
            'data': ''
        })

@csrf_exempt
def get_pet_info_from_id(request):
    if request.user.is_authenticated and request.method == "POST":
        data = list(pet.objects.filter(pet_id=request.POST['pet_id']).values(
            'pet_id','state','primary_breed','secondary_breed',
            'primary_color','secondary_color1','secondary_color2',
            'rescuer_name','publisher_name','pet_type','pet_name',
            'pet_age','maturity_size','gender','fur_length',
            'vaccinated','dewormed','sterilized','health',
            'quantity','fee','video_amt','photo_amt','description',
            'adoption_speed','popularity_star','adoption_star'))
        # return JsonResponse(data, safe=False)
        if(len(data)!=0):
            return JsonResponse({
                'success':           1,
                'data':             data,
            })
        else:
            return JsonResponse({
                'success':           0,
                'data':             "incorrect pet id",
            })
    else:
        return JsonResponse({
            'success':           0,
            'data':             "wrong method",
        })
