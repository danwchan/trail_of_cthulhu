from django.contrib import admin
from .models import AbilityList, AbilityExamples, OccupationList, DriveList, DriveExamples, AssociatedOccuDrive, AssociatedOccuAbil

# Register your models here.

admin.site.register(AbilityList)
admin.site.register(AbilityExamples)
admin.site.register(OccupationList)
admin.site.register(DriveList)
admin.site.register(DriveExamples)
admin.site.register(AssociatedOccuDrive)
admin.site.register(AssociatedOccuAbil)
