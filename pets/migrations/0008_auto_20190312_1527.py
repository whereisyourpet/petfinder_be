# Generated by Django 2.1.7 on 2019-03-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20190312_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.CharField(default='发布者很懒，什么都没有说', max_length=9000, verbose_name='描述'),
        ),
    ]
