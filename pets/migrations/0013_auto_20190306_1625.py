# Generated by Django 2.1.7 on 2019-03-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0012_auto_20190306_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet_info',
            name='primary_breed',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Affenpinscher'), (2, 'Afghan Hound'), (3, 'Airedale Terrier')], default=None, max_length=200, verbose_name='主要血统'),
        ),
        migrations.AlterField(
            model_name='pet_info',
            name='primary_color',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Black'), (2, 'Brown'), (3, 'Golden'), (4, 'Yellow'), (5, 'Cream'), (6, 'Gray'), (7, 'White')], default=None, verbose_name='主要毛色'),
        ),
        migrations.AlterField(
            model_name='pet_info',
            name='secondary_breed',
            field=models.IntegerField(blank=True, choices=[(0, 'None'), (1, 'Affenpinscher'), (2, 'Afghan Hound'), (3, 'Airedale Terrier')], default='None', verbose_name='次要血统'),
        ),
        migrations.AlterField(
            model_name='pet_info',
            name='secondary_color1',
            field=models.IntegerField(blank=True, choices=[(0, 'None'), (1, 'Black'), (2, 'Brown'), (3, 'Golden'), (4, 'Yellow'), (5, 'Cream'), (6, 'Gray'), (7, 'White')], default='None', verbose_name='次要毛色1'),
        ),
        migrations.AlterField(
            model_name='pet_info',
            name='secondary_color2',
            field=models.IntegerField(blank=True, choices=[(0, 'None'), (1, 'Black'), (2, 'Brown'), (3, 'Golden'), (4, 'Yellow'), (5, 'Cream'), (6, 'Gray'), (7, 'White')], default='None', verbose_name='次要毛色2'),
        ),
    ]