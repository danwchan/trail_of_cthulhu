# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthcharacter', '0005_auto_20170617_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abilitylist',
            name='investigative_type',
            field=models.CharField(choices=[('A', 'Academic ability'), ('I', 'Interpersonal abilty'), ('T', 'Technical ability')], max_length=1),
        ),
    ]
