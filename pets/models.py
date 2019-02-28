from django.db import models

# Create your models here.

class breed:
    # choice of breed
    BREED_TYPE_CHOICE = (
        ('Felinae',     '短毛猫'),
        ('Persian',     '波斯猫'),
        ('DragonLi',    '狸花猫'),
    )

    # PK
    breed_id        = models.IntegerField(max_length=15)

    # others
    breed_type      = models.CharField(max_length=15, choices=BREED_TYPE_CHOICE)

class color:
    # choice of color
    COLOR_TYPE_CHOICE = (
        ('B', 'Blue'),
        ('R', 'Red'),
        ('G', 'Green')
    )

    # PK
    color_id        = models.IntegerField(max_length=15)

    # others
    color_type      = models.CharField(max_length=15, choices=COLOR_TYPE_CHOICE)


class pet_info(models.Model):
    # constant
    DEFAULT_MAXLENGTH = 15

    # choices
    # choice of pet type
    PET_TYPE_CHOICE = (
        ('1','Dog'),
        ('2','Cat'),
    )
    # choice of MaturitySize 
    MATURITY_SIZE_TYPE = (
        ('0', 'Not Specified'),
        ('1', 'Small'),
        ('2', 'Medium'),
        ('3', 'Large'),
        ('4', 'Extra Large'),
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
        ('1','Yes'),
        ('2','No'),
        ('3','Not Sure'),
    )
    # choice of Dewormed 
    DEWORMED_CHOICE = (
        ('1','Yes'),
        ('2','No'),
        ('3','Not Sure'),
    )
    # choice of Vaccinated 
    VACCINATED_CHOICE = (
        ('1','Yes'),
        ('2','No'),
        ('3','Not Sure'),
    )

    # PK and FK
    pet_id          = models.IntegerField(
                            max_length      = DEFAULT_MAXLENGTH, 
                            primary_key     = True,
                            verbose_name    = "宠物ID",)
    breed_id        = models.ForeignKey(
                            breed, 
                            on_delete       = models.CASCADE,
                            verbose_name    = "血统ID",)
    color_id        = models.ForeignKey(
                            color, 
                            on_delete       = models.CASCADE,
                            verbose_name    = "颜色ID",)

    # unknow relationship
    rescuer_id      = models.IntegerField(
                            max_length      = DEFAULT_MAXLENGTH,
                            verbose_name    = "救助者ID",)
    publisher_id    = models.IntegerField(
                            max_length      = DEFAULT_MAXLENGTH,
                            verbose_name    = "发布者ID",)

    # orther infomation
    pet_type        = models.CharField(
                            max_length      = 1,
                            choices         = PET_TYPE_CHOICE,
                            verbose_name    = "动物类型",)
    pet_name        = models.CharField(
                            max_length      = 50,
                            verbose_name    = "动物名称",)
    pet_age         = models.IntegerField(
                            max_length      = 2,
                            verbose_name    = "动物年龄",)
    maturity_size   = models.IntegerField(
                            max_length      = 1,
                            choices         = MATURITY_SIZE_TYPE,
                            verbose_name    = "动物体型",)
    gender          = models.CharField(
                            max_length      = 1, 
                            choices         = GENDER_CHOICE,
                            verbose_name    = "动物性别",)
    fur_length      = models.IntegerField(
                            max_length      = 5,
                            verbose_name    = "毛长",)
    vaccinated      = models.BooleanField(
                            max_length      = 1,
                            choices         = VACCINATED_CHOICE,
                            verbose_name    = "是否接受疫苗",)
    dewormed        = models.BooleanField(
                            max_length      = 1,
                            choices         = DEWORMED_CHOICE,
                            verbose_name    = "是否已除虫",)
    sterilized      = models.BooleanField(
                            max_length      = 1,
                            choices         = STERILIZED_CHOICE,
                            verbose_name    = "是否已消毒",)
    health          = models.CharField(
                            max_length      = 1,
                            choice          = HEALTH_CHOICE,
                            verbose_name    = "健康程度",)
    quantity        = models.IntegerField(
                            max_length=3)
    fee             = models.DecimalField(
                            verbose_name    = "收养费",)
    state           = models.CharField(
                            max_length      = 200,
                            verbose_name    = "州位置",)
    video_amt       = models.CharField(
                            max_length      = DEFAULT_MAXLENGTH,
                            verbose_name    = "视频",)
    photo_amt       = models.CharField(
                            max_length      = DEFAULT_MAXLENGTH,
                            verbose_name    = "照片")
    description     = models.CharField(
                            max_length      = 500,
                            verbose_name    = "描述",)
    adoption_speed  = models.IntegerField(
                            max_length      = 3, 
                            verbose_name    = "被收养速率",
                            )

    