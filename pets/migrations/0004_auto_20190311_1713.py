# Generated by Django 2.1.7 on 2019-03-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20190311_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='宠物ID'),
        ),
    ]