# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthcharacter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupationlist',
            name='credit_lower',
            field=models.IntegerField(verbose_name='the lower limit of the credit rating'),
        ),
        migrations.AlterField(
            model_name='occupationlist',
            name='credit_upper',
            field=models.IntegerField(verbose_name='the upper limit of the credit rating'),
        ),
        migrations.AlterField(
            model_name='revisionstatus',
            name='rating',
            field=models.IntegerField(default=3, verbose_name='a rating number where 1 is the best and 5 requires a rewite'),
        ),
    ]
