from django.contrib import admin
from .models import BirthForm, InnateAbility, Campaign, Session, SanityPillars, StabilitySources

# Inline projects to build the editing forms
class AbilityInLine(admin.StackedInline):
    model = InnateAbility
    fk_name = 'character_id'
    extra = 0

class CharacterInLine(admin.StackedInline):
    model = BirthForm
    fk_name = 'drive'
    extra = 0

class BirthAdmin(admin.ModelAdmin):
    list_display = ['name', 'drive', 'occupation']
    search_fields = ['BirthForm__name']
    inlines = [
        AbilityInLine,
    ]

# Register your models here.

admin.site.register(BirthForm, BirthAdmin)

#To BUILD
#session manager / scheduler
