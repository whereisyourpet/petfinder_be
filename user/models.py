from django.db import models

# Create your models here.


class UserAccount(models.Model):
    userID = models.AutoField()
    username = models.CharField(max_length=16, verbose_name='用户名')
    nickname = models.CharField(max_length=16, verbose_name='昵称')
    password = models.CharField(max_length=128, verbose_name='密码')

    def __str__(self):
        return self.username
