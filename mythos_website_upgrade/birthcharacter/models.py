from django.db import models
from randomslugfield import RandomSlugField

class RevisionStatus(models.Model):
    created = models.DateTimeField('the date this record was created',auto_now=True)
    updated = models.DateTimeField('the last point this record was updated',auto_now_add=True)
    original = models.BooleanField('this record is directly from the Trail of Cthulhu, needs rewite')
    comments = models.TextField('comments which have been associated with this record',
        blank = True)
    RATING_CHOICES = (
        (1, 'works well'),
        (2, 'few complaints'),
        (3, 'neutral'),
        (4, 'some concerns'),
        (5, 'might be broken')
    )
    rating = models.IntegerField('1: works well, \n 5: needs rewite',default=3)
    purist = models.BooleanField()
    pulp = models.BooleanField()
    
 #   def __str__(self):
 #       return str(self.)    

class OccupationList(RevisionStatus):
    occupation = models.CharField('name',max_length=50, primary_key=True)
    credit_lower = models.IntegerField('the lower limit of the credit rating')
    credit_upper = models.IntegerField('the upper limit of the credit rating')
    description = models.TextField('what is this occupation?')

    def __str__(self):
        return self.occupation    
    
class SpecialList(RevisionStatus):
    occupation = models.ForeignKey(
        OccupationList,
        default = 'unassigned_special',
        on_delete = models.SET_DEFAULT
    )
    special = models.TextField('the special benefits rendered onto a character of this occupation')

class DriveList(RevisionStatus):
    drive = models.CharField('name',max_length=25, primary_key=True)
    description = models.TextField()
    
    def __str__(self):
        return self.drive

class DriveExamples(RevisionStatus):
    drive = models.ForeignKey(
        DriveList,
        default = 'unassigned_example',
        on_delete = models.SET_DEFAULT,
    )
    example_quote = models.TextField('a quote from a novel which exemplifies the drive')
    example_character = models.CharField('a character who exemplifies the drive', max_length=50)
    MEDIA_TYPE_CHOICES = (
        ('C', 'cinema'),
        ('R', 'radio'),
        ('G', 'comic'),
        ('N', 'novel')
    )
    example_media = models.CharField(
        max_length = 1,
        choices = MEDIA_TYPE_CHOICES
    )

class AbilityList(RevisionStatus):
    ability = models.CharField('the name of the ability',max_length=50, primary_key=True)
    MAJOR_TYPE_CHOICES = (
        ('I', 'Investigative abiity'),
        ('G', 'General ability')
    )
    major_type = models.CharField(
        max_length = 1,
        choices = MAJOR_TYPE_CHOICES
    )
    INVESTIGATIVE_TYPE_CHOICES = (
        ('A', 'Academic ability'),
        ('I', 'Interpersonal abilty'),
        ('T', 'Technical ability'),
        ('D', 'Doubles as an investigative ability')
    )
    investigative_type = models.CharField(
        max_length =1,
        choices = INVESTIGATIVE_TYPE_CHOICES,
        blank = True
    )
    description = models.TextField()
    
    def __str__(self):
        return self.ability
    
class AbilityExamples(RevisionStatus):
    ability = models.ForeignKey(
        AbilityList,
        default = 'unassigned_example',
        on_delete = models.SET_DEFAULT,
    )
    examples = models.TextField('examples of how an ability is used to advance the story')


class AssociatedOccuDrive (RevisionStatus):
#recommended drives for the occupation, but anything goes really!
    drive = models.ForeignKey(
        DriveList,
        default = 'none',
        on_delete = models.CASCADE
    )    
    associated_occupations = models.ForeignKey(
        OccupationList,
        default = 'none',
        on_delete=models.CASCADE
    )    

class AssociatedOccuAbil(RevisionStatus):
#the associations which allow certain occupations to gain 2 rating points for each build point
    occupational_abilities = models.ForeignKey(
        AbilityList,
        default = 'none',
        on_delete = models.CASCADE
    )
    associated_occupations = models.ForeignKey(
        OccupationList,
        default = 'none',
        on_delete=models.CASCADE
    )
    conditional_options = models.CharField('any restrictions or modifiers',
        max_length = 75,
        blank = True)
    #for example conditional_options may restrict occupational abilities to a sub class of occupation, or they may specifiy choosing from a pool which should be represented as choose X from a pool of Y: X, logic for implementing the choices will have to reside in the character selection validation
    ability_options = models.IntegerField('this association is for a choice from several options, choose X',
        blank = True,
        null = True
    )
    options_pool = models.IntegerField('this association is for a choice from several options, from Y',
        blank = True,
        null = True
    )

class BirthForm(models.Model):
    birthcode = RandomSlugField(length=7)
