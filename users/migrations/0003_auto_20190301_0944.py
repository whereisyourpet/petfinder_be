# Generated by Django 2.1.7 on 2019-03-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190228_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='married',
            field=models.BooleanField(default=False, verbose_name='是否已婚'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, verbose_name='电话'),
        ),
    ]