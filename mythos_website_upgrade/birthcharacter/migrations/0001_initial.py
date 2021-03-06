# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 00:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import randomslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirthForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthcode', randomslugfield.fields.RandomSlugField(blank=True, editable=False, length=7, max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RevisionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='the date this record was created')),
                ('updated', models.DateTimeField(auto_now_add=True, verbose_name='the last point this record was updated')),
                ('original', models.BooleanField(verbose_name='is this record from the Trail of Cthulhu or has it been reworked for the new modern day setting?')),
                ('comments', models.TextField(verbose_name='comments which have been associated with this record')),
                ('rating', models.IntegerField(default=3, max_length=1, verbose_name='a rating number where 1 is the best and 5 requires a rewite')),
                ('purist', models.BooleanField(verbose_name='is this relevant for purist settings')),
                ('pulp', models.BooleanField(verbose_name='is this relevant for pulp settings')),
            ],
        ),
        migrations.CreateModel(
            name='AbilityExamples',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birthcharacter.RevisionStatus')),
                ('examples', models.TextField(verbose_name='examples of how an ability is used to advance the story')),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.CreateModel(
            name='AbilityList',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='birthcharacter.RevisionStatus')),
                ('ability', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='the name of the ability')),
                ('major_type', models.CharField(choices=[('I', 'Investigative abiity'), ('G', 'General ability')], max_length=1)),
                ('investigative_type', models.CharField(choices=[('I', 'Investigative abiity'), ('G', 'General ability')], max_length=1)),
                ('description', models.TextField()),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.CreateModel(
            name='AssociatedOccuAbil',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birthcharacter.RevisionStatus')),
                ('ability', models.CharField(max_length=50, verbose_name='the name of the ability for which an occupation can spend a single build point for 2 rating points')),
                ('occupation', models.CharField(max_length=50, verbose_name='the name of the occupation for which a single build point grants 2 rating points for this ability')),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.CreateModel(
            name='AssociatedOccuDrive',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birthcharacter.RevisionStatus')),
                ('drive', models.CharField(max_length=25, verbose_name='the name of the drive associated with the ocupations')),
                ('occupation', models.CharField(max_length=50, verbose_name='the name of the occupation associated with an ability')),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.CreateModel(
            name='DriveExamples',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birthcharacter.RevisionStatus')),
                ('example_quote', models.TextField(verbose_name='a quote from a novel which exemplifies the drive')),
                ('example_character', models.CharField(max_length=50, verbose_name='a character who exemplifies the drive')),
                ('example_media', models.CharField(choices=[('C', 'cinema'), ('R', 'radio'), ('G', 'comic'), ('N', 'novel')], max_length=1)),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.CreateModel(
            name='DriveList',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='birthcharacter.RevisionStatus')),
                ('drive', models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='the name of the drive')),
                ('description', models.TextField()),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.CreateModel(
            name='OccupationList',
            fields=[
                ('revisionstatus_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='birthcharacter.RevisionStatus')),
                ('occupation', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='the name of the occupation')),
                ('credit_lower', models.IntegerField(max_length=1, verbose_name='the lower limit of the credit rating')),
                ('credit_upper', models.IntegerField(max_length=1, verbose_name='the upper limit of the credit rating')),
                ('special', models.TextField(verbose_name='the special benefits rendered onto a character of this occupation')),
                ('description', models.TextField(verbose_name='what is this occupation?')),
                ('occupational_abilities', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='birthcharacter.AssociatedOccuAbil')),
            ],
            bases=('birthcharacter.revisionstatus',),
        ),
        migrations.AddField(
            model_name='driveexamples',
            name='drive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='birthcharacter.DriveList'),
        ),
        migrations.AddField(
            model_name='abilitylist',
            name='associated_occupations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='birthcharacter.AssociatedOccuAbil'),
        ),
        migrations.AddField(
            model_name='abilityexamples',
            name='ability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='birthcharacter.AbilityList'),
        ),
    ]
