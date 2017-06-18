from django.contrib import admin
from .models import AbilityList, AbilityExamples, OccupationList, DriveList, DriveExamples, AssociatedOccuDrive, AssociatedOccuAbil, SpecialList

# Primary keys you care about
#primary_keys = [
#    'occupation',
#    'drive',
#    'ability'
#    ]

# Inline projects to build the editing forms
class AbilityInLine(admin.TabularInline):
    model = AssociatedOccuAbil
    fk_name = 'associated_occupations'
    extra = 0

# ModelAdmin classes to bind it all together representing editing forms

class AbilityAdmin(admin.ModelAdmin):
    list_display = ['ability', 'purist', 'pulp', 'rating']
    
class OccupationAdmin(admin.ModelAdmin):
    list_display = ['occupation', 'purist', 'pulp', 'rating']
    search_fields = ['occupationlist__occupation']
    inlines = [
        AbilityInLine
    ]
    
    def _abilitylist(self, obj):
        return obj.abilitylist.all().count()

class DriveAdmin(admin.ModelAdmin):
    list_display = ['drive', 'purist', 'pulp', 'rating']

class AbilityExAdmin(admin.ModelAdmin):
    list_display = ['get_ability', 'purist', 'pulp', 'rating']
    
    def get_ability(self, obj):
        return obj.abilitylist.ability
    get_ability.short_description = 'Ability'

# Register your models here.

admin.site.register(AbilityList, AbilityAdmin)
admin.site.register(AbilityExamples, AbilityExAdmin)
admin.site.register(OccupationList, OccupationAdmin)
admin.site.register(SpecialList)
admin.site.register(DriveList, DriveAdmin)
admin.site.register(DriveExamples)
