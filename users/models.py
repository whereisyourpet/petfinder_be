from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    location = models.CharField(max_length=200, verbose_name='地址', blank=True)
    has_pet = models.BooleanField(verbose_name='是否有宠物', default=False)
    willing = models.BooleanField(verbose_name='收养意愿', default=False)
    number = models.IntegerField(verbose_name="收养个数", default=0)
    married = models.BooleanField(verbose_name="是否已婚", default=False)
    phone = models.CharField(max_length=12, verbose_name="电话", blank=True)
    gender = models.BooleanField(
        '性别', max_length=1, choices=((0, '男'), (1, '女'),), default=0)
    description = models.CharField(
        max_length=300, verbose_name="个性签名", default="这个人很懒，什么都没有留下")

    class Meta(AbstractUser.Meta):
        pass
