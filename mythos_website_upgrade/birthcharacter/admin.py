from django.contrib import admin
from .models import AbilityList, AbilityExamples, OccupationList, DriveList, DriveExamples, AssociatedOccuDrive, AssociatedOccuAbil, SpecialList

# Primary keys you care about
#primary_keys = [
#    'occupation',
#    'drive',
#    'ability'
#    ]

# Inline projects to build the editing forms
class AbilityInLine(admin.StackedInline):
    model = AssociatedOccuAbil
    fk_name = 'associated_occupations'
    extra = 0

class OccuInLine(admin.StackedInline):
    model = AssociatedOccuDrive
    fk_name = 'drive'
    extra = 0

class AbilityExInLine(admin.StackedInline):
    model = AbilityExamples
    fk_name = 'ability'
    extra = 0

class DriveExInLine(admin.StackedInline):
    model = DriveExamples
    fk_name = 'drive'
    extra = 0

# ModelAdmin classes to bind it all together representing editing forms

class AbilityAdmin(admin.ModelAdmin):
    list_display = ['ability', 'purist', 'pulp', 'rating']
    search_fields = ['abilitylist__ability']
    inlines = [
        AbilityExInLine
    ]    
    
class OccupationAdmin(admin.ModelAdmin):
    list_display = ['occupation', 'purist', 'pulp', 'rating']
    search_fields = ['occupationlist__occupation']
    inlines = [
        AbilityInLine
    ]
    
    def _abilitylist(self, obj):
        return obj.abilitylist.all().count() #just copied this over... I don't know what it does :P

class DriveAdmin(admin.ModelAdmin):
    list_display = ['drive', 'purist', 'pulp', 'rating']
    search_fields = ['abilitylist__ability']
    inlines = [
        DriveExInLine,
        OccuInLine
    ]

# Register your models here.

admin.site.register(AbilityList, AbilityAdmin)
admin.site.register(OccupationList, OccupationAdmin)
admin.site.register(DriveList, DriveAdmin)

#TO BUILD
#overview page to see which records are old/poorly perofrming
#formatting to make it prettier
#expand drive examples to all entries and formalize the media source idea
