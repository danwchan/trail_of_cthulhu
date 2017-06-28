from django.shortcuts import render
from django.views.generic import DetailView, ListView

from birthcharacter.models import OccupationList, AssociatedOccuAbil

# Create your views here.

def occupation_list(request):
    occupations = OccupationList.objects.all()
    return render(request, 'characterbirther/make_investigator.html', {'occupations' : occupations})

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
