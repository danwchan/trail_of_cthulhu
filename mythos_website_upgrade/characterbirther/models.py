from django.db import models
from randomslugfield import RandomSlugField
from birthcharacter.models import AbilityList, OccupationList, DriveList, RevisionStatus


#BirthForm model is responsible for holding the created player characters
class BirthForm(models.Model):
    birthcode = RandomSlugField(length=7, primary_key = True)
    name = models.CharField('the Name of your investigator', max_length = 50)
    occupation = models.ForeignKey(
        OccupationList,
        on_delete = models.PROTECT
    )
    drive = models.ForeignKey(
        DriveList,
        on_delete = models.PROTECT
    )
    birthplace = models.CharField('the place where the character is born', max_length=25)
    
#InnateAbility model is responsible for holding the values of created players skills
class InnateAbility(models.Model):
    character_id = models.ForeignKey(
        BirthForm,
        on_delete = models.CASCADE
    )
    ability = models.ForeignKey(
        AbilityList,
        on_delete = models.PROTECT
    )
    value = models.IntegerField()

#the session model
class Session(models.Model):
    sessioncode = models.CharField(
        'the affectionate name of the session', 
        max_length=25, 
        primary_key = True
    )
    investigators = models.ManyToManyField(BirthForm)
    date = models.DateField('the date the session took place')
    plot = models.TextField('what happened during the session?')

#Campaign model is the responsible for holding the information describing what happened in each campaign, with a MAX of 5 player characters but perhaps with more and max of 3 sessions.
class Campaign(models.Model):
    campaigncode = models.CharField(
        'the affectionate name of the campaign in which unites characters on a Spine',
        max_length = 25,
        primary_key = True,
    )
    session1 = models.OneToOneField(
        Session,
        on_delete = models.PROTECT,
        blank = True,
        related_name = 'first_session_of'
    )
    session2 = models.OneToOneField(
        Session,
        on_delete = models.PROTECT,
        blank = True,
        related_name = 'second_session_of'
    )
    session3 = models.OneToOneField(
        Session,
        on_delete = models.PROTECT,
        blank = True,
        related_name = 'third_session_of'
    )
    synopsis = models.TextField('a short description of the campaign: what changed, if anything, in the world?')
    complete = models.BooleanField('campaign complete')

#SanityPillars model is responsible for holding the created players pillars of sanity
class SanityPillars(RevisionStatus):
    investigators = models.ForeignKey(
        BirthForm,
        on_delete = models.PROTECT
    )
    pillar = models.CharField('pillar of sanity',max_length=30)
    description = models.TextField(
        'a short description of this pillar of sanity',
        blank = True
    )
    
#StabilitySources model is responsible for holdng the created players sources of stability, could this area be expanded a little to involve these as more stable NPCs?
class StabilitySources(RevisionStatus):
    investigators = models.ForeignKey(
        BirthForm,
        on_delete = models.PROTECT
    )
    name = models.CharField('the Name of this source of stability', max_length = 50)
    residence = models.CharField(
        'where this source lives',
        max_length = 50,
        blank = True
    )
    relation = models.CharField('the relationship between the investigator and this source of stability', max_length = 50)
    personality = models.TextField(
        'a short description of the personality of this character',
        blank = True)
