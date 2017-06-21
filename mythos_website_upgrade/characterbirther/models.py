from django.db import models
from randomslugfield import RandomSlugField
from birthcharacter import AbilityList


#BirthForm model is responsible for holding the created player characters
class BirthForm(models.Model):
    birthcode = RandomSlugField(length=7, primary_key = True)
    name = models.CharField('the Name of your investigator', max_length = 50)
    occupation = models.ForeignKey(
        OccupationList,
        on_delete = models.PROTECT
    )
    birthplace = models.CharField('the place where the character is born', max_length=25)
    
#InnateAbility model is responsible for holding the created players skills
class InnateAbility(models.Model):
    character_id = models.ForeignKey(
        BirthForm,
        on_delete.PROTECT
    )
    ability = models.ForeignKey(
        AbilityList,
        on_delete.PROTECT
    )
    value = models.IntegerField()
    
#CharacterFibre model is responsible for holding the created players pillars of sanity
class InnateAbility

#Campaign model is the responsible for holding the information describing what happened in each campaign, with a MAX of 5 player characters but perhaps with more and max of 3 sessions.
class Campaign(models.Model):
    campaigncode = models.CharField(
        'the affectionate name of the campaign in which unites characters on a Spine',
        primary_key = True,
    )
    session1 = models.ForeignKey(
        Session,
        on_delete = models.CASCADE,
        blank = True,
        unique = True
    )
    session2 = models.ForeignKey(
        Session,
        on_delete = models.CASCADE,
        blank = True,
        unique = True
    )
    session3 = models.ForeignKey(
        Session,
        on_delete = models.CASCADE,
        blank = True,
        unique = True
    )
    synopsis = models.TextField('a short description of the campaign: what changed, if anything, in the world?')
    complete = models.BooleanField('campaign complete')

#the session model
class Session(models.Model):
    sessioncode = models.CharField('the affectionate name of the session', max_length=25, primary_key = True)
    investigators = models.ManyToManyField(BirthForm)
    date = date.Field('the date the session took place')
    plot = models.TextField('what happened during the session?')
