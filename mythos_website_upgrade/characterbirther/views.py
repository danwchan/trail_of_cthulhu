from django.shortcuts import render
from django.views.generic import DetailView, ListView

from birthcharacter.models import OccupationList, AbilityList, DriveList, AssociatedOccuAbil

# Create your views here.

def browse_options(request):
    occupations = OccupationList.objects.all()
    abilities = AbilityList.objects.all()
    drives = DriveList.objects.all()
    drive_2_occupation = AssociatedOccuAbil.objects.all()
    #DriveList.objects.filter(associatedoccudrive__drive = 'Antiquarian')
    data_aliases = {'occupations' : occupations,
                    'abilities' : abilities,
                    'drives' : drives,
                    'recommended_occupations' : drive_2_occupation,
                    }
    return render(request, 'characterbirther/make_investigator.html', data_aliases)

#for the python debug toolbar
    
'''
some general view templates that are over your head at the moment

class Occupations(ListView):
    model = OccupationList
    template_name = 'characterbirther/make_investigator.html'
    
    def get_context_data(self ,**kwargs):
        # Call the base using super to access the context data
        context = super(Occupations,self).get_context_data(**kwargs)
        # Assign data to the context data
        context['occupational_abilities'] = AssociatedOccuAbil.objects.all()
        return context

class CharacterOptionsView(DetailView):
    model = OccupationList
    template_name = 'characterbirther/make_investigator.html'
    
    def get_context_data(self ,**kwargs):
        # Call the base using super to access the context data
        context = super(CharacterOptionsView,self).get_context_data(**kwargs)
        # Assign data to the context data
        context['occupational_abilities'] = AssociatedOccuAbil.objects.all()
        return context
'''
