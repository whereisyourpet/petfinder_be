from django.db import models

# Create your models here.

class breed:
    pass

class color:
    pass


class pet_info(models.Model):
    # constant
    DEFAULT_MAXLENGTH = 15

    # choice of gender
    GENDER_CHOICE = (
        ('M','Male'),
        ('F','Female'),
    )

    # PK and FK
    pet_id          = models.IntegerField(max_length=DEFAULT_MAXLENGTH, primary_key=True)
    breed_id        = models.ForeignKey(breed, on_delete=models.CASCADE)
    color_id        = models.IntegerField(max_length=DEFAULT_MAXLENGTH)

    # unknow relationship
    rescuer_id      = models.IntegerField(max_length=DEFAULT_MAXLENGTH)
    publisher_id    = models.IntegerField(max_length=DEFAULT_MAXLENGTH)

    # orther infomation
    pet_type        = models.CharField(max_length=50)
    pet_name        = models.CharField(max_length=50)
    pet_age         = models.IntegerField(max_length=2)
    maturity_size   = models.IntegerField(max_length=2)
    gender          = models.CharField(max_length=1, choices=GENDER_CHOICE)
    fur_length      = models.IntegerField(max_length=5)
    vaccinated      = models.BooleanField()
    dewormed        = models.BooleanField()
    sterilized      = models.BooleanField()
    health          = models.CharField(max_length=DEFAULT_MAXLENGTH)
    quantity        = models.IntegerField(max_length=3)
    fee             = models.DecimalField()
    state           = models.CharField(max_length=200)
    video_amt       = models.CharField(max_length=DEFAULT_MAXLENGTH)
    photo_amt       = models.CharField(max_length=DEFAULT_MAXLENGTH)
    description     = models.CharField(max_length=500)
    adoption_speed  = models.IntegerField(max_length=3)

    