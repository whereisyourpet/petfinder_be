# Generated by Django 2.1.7 on 2019-03-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0010_auto_20190306_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_info',
            name='pet_type',
            field=models.IntegerField(choices=[(1, 'Dog'), (2, 'Cat')], verbose_name='动物类型'),
        ),
    ]
