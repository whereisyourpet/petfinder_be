from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class pet_info(models.Model):
    # constant
    DEFAULT_MAXLENGTH = 15

    # choices
    # choice of pet color
    COLOR_CHOICE    = (
        ('B', 'Blue'),
        ('R', 'Red'),
        ('G', 'Green'),
    )
    # choice of breed
    BREED_TYPE_CHOICE = (
        ('Felinae',     '短毛猫'),
        ('Persian',     '波斯猫'),
        ('DragonLi',    '狸花猫'),
    )
    # choice of pet type
    PET_TYPE_CHOICE = (
        ('1','Dog'),
        ('2','Cat'),
    )
    # choice of MaturitySize 
    MATURITY_SIZE_TYPE = (
        (0, 'Not Specified'),
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
        (4, 'Extra Large'),
    )
    # choice of gender
    GENDER_CHOICE = (
        ('1','Male'),
        ('2','Female'),
        ('3','Mixed, if profile represents group of pets'),
    )
    # choice of fur length
    FURLENGTH_CHOICE = (
        ('0','Not Specified'),
        ('1','Short'),
        ('2','Medium'),
        ('3','Long'),
    )
    # choice of health
    HEALTH_CHOICE = (
        ('0','Not Specified'),
        ('1','Healthy'),
        ('2','Minor Injury'),
        ('3','Serious Injury'),
    )
    # choide of Sterilized
    STERILIZED_CHOICE = (
        (1,'Yes'),
        (2,'No'),
        (3,'Not Sure'),
    )
    # choice of Dewormed 
    DEWORMED_CHOICE = (
        (1,'Yes'),
        (2,'No'),
        (3,'Not Sure'),
    )
    # choice of Vaccinated 
    VACCINATED_CHOICE = (
        (1,'Yes'),
        (2,'No'),
        (3,'Not Sure'),
    )
    # choice of fur length
    FUR_LENGTH_CHOICE = (
        (1, 'Short'),
        (2, 'Medium'),
        (3, 'Long'),
        (0, 'Not Specified'),
    )

    # PK and FK
    # 如果不使用自动生成的id，则取消如下代码注释
    # see: https://docs.djangoproject.com/en/2.1/topics/db/models/#automatic-primary-key-fields
    pet_id          = models.AutoField(
                            primary_key     = True,
                            verbose_name    = "宠物ID",)
   
    rescuer_name    = models.CharField(
                            max_length      = 30,
                            verbose_name    = "救助者姓名",
                            default         = None,
                            blank           = True,)
    publisher_name  = models.CharField(
                            max_length      = 30,
                            verbose_name    = "发布者姓名",
                            default         = None,)

    pet_type        = models.IntegerField(
                            choices         = PET_TYPE_CHOICE,
                            verbose_name    = "动物类型",
                            default         = None,)
    pet_name        = models.CharField(
                            max_length      = 50,
                            verbose_name    = "动物名称",
                            default         = None,)
    pet_age         = models.IntegerField(
                            verbose_name    = "动物年龄",
                            default         = 0,
                            blank           = True,)
    maturity_size   = models.IntegerField(
                            choices         = MATURITY_SIZE_TYPE,
                            verbose_name    = "动物体型",
                            default         = 0,
                            blank           = True,)
    gender          = models.IntegerField(
                            choices         = GENDER_CHOICE,
                            verbose_name    = "动物性别",
                            default         = '3',)
    fur_length      = models.IntegerField(
                            choices         = FUR_LENGTH_CHOICE,
                            verbose_name    = "毛长",
                            default         = 0,
                            blank           = True,)
    vaccinated      = models.IntegerField(
                            choices         = VACCINATED_CHOICE,
                            verbose_name    = "是否接受疫苗",
                            default         = 3,)
    dewormed        = models.IntegerField(
                            choices         = DEWORMED_CHOICE,
                            verbose_name    = "是否已除虫",
                            default         = 3,)
    sterilized      = models.IntegerField(
                            choices         = STERILIZED_CHOICE,
                            verbose_name    = "是否已消毒",
                            default         = 3,)
    health          = models.IntegerField(
                            choices         = HEALTH_CHOICE,
                            verbose_name    = "健康程度",
                            default         = 3,)
    quantity        = models.DecimalField(
                            max_digits      = 5, 
                            decimal_places  = 2,
                            verbose_name    = "体重",
                            default         = 0,
                            blank           = True,)
    fee             = models.DecimalField(
                            max_digits      = 5, 
                            decimal_places  = 2, 
                            verbose_name    = "收养费",
                            default         = 0,)
    state           = models.CharField(
                            max_length      = 200,
                            verbose_name    = "州位置",
                            default         = 'None',
                            blank           = True,)
    video_amt       = models.IntegerField(
                            verbose_name    = "视频",
                            default         = 'None',
                            blank           = True,)
    photo_amt       = models.IntegerField(
                            verbose_name    = "照片",
                            default         = 'None',
                            blank           = True,)
    description     = models.CharField(
                            max_length      = 500,
                            verbose_name    = "描述",
                            default         = "发布者很懒，什么都没有说",)
    adoption_speed  = models.IntegerField(
                            verbose_name    = "被收养速率",
                            default         = 0,
                            blank           = True,)
    primary_breed   = models.CharField(
                            max_length      = 200,
                            choices         = BREED_TYPE_CHOICE,
                            verbose_name    = "主要血统",
                            default         = 'None',)
    secondary_breed = models.CharField(
                            max_length      = 200, 
                            choices         = BREED_TYPE_CHOICE,
                            verbose_name    = "次要血统",
                            default         = None,
                            blank           = True,)
    primary_color   = models.CharField(
                            max_length      = 10,
                            verbose_name    = "主要毛色",
                            default         = None,)
    secondary_color1= models.CharField(
                            max_length      = 10,
                            verbose_name    = "次要毛色1",
                            default         = None,
                            blank           = True,)
    secondary_color2= models.CharField(
                            max_length      = 10,
                            verbose_name    = "次要毛色2",
                            default         = None,
                            blank           = True,)

