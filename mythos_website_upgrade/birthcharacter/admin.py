from django.contrib import admin
from .models import AbilityList, AbilityExamples, OccupationList, DriveList, DriveExamples, AssociatedOccuDrive, AssociatedOccuAbil, SpecialList

# Primary keys you care about
#primary_keys = [
#    'occupation',
#    'drive',
#    'ability'
#    ]

# Some ModelAdmin classes to bind it all together

class AbilityAdmin(admin.ModelAdmin):
    list_display = ('ability',)

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('occupation',)

class DriveAdmin(admin.ModelAdmin):
    list_display = ('drive',)

    
# Register your models here.

admin.site.register(AbilityList, AbilityAdmin)
admin.site.register(AbilityExamples)
admin.site.register(OccupationList, OccupationAdmin)
admin.site.register(SpecialList)
admin.site.register(DriveList, DriveAdmin)
admin.site.register(DriveExamples)
admin.site.register(AssociatedOccuDrive)
admin.site.register(AssociatedOccuAbil)
