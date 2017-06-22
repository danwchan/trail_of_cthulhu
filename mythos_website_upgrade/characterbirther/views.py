from django.shortcuts import render
from birthcharacter.models import OccupationList
# Create your views here.

def make_investigator(request):
    occupations = OccupationList.objects.all()
    return render(request, 'characterbirther/make_investigator.html', {'occupations' : occupations})
