from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

from formtools.wizard.views import NamedUrlSessionWizardView

from birthcharacter.models import OccupationList, AbilityList, DriveList, AssociatedOccuAbil, AssociatedOccuDrive
from characterbirther.forms import CharBirthForm, DriveForm, PillarsOfSanity, OccupationForm, Abilities, SourcesOfStability

DATA_ALIASES = {'occupations' : OccupationList.objects.all(),
                'abilities' : AbilityList.objects.all(),
                'I_abilities' : AbilityList.objects.filter(major_type='I'),
                'G_abilities' : AbilityList.objects.filter(major_type='G'),
                'drives' : DriveList.objects.all(),
                'recommended_occupations' : AssociatedOccuAbil.objects.all(),
                'birth_form' : CharBirthForm(),
                }

TEMPLATES =  {'' : 'characterbirther/make_investigator.html',
              'drive' : 'characterbirther/choose_psych.html',
              'pillars' : 'characterbirther/choose_pillars.html',
              'occupation' : 'characterbirther/choose_occupations.html',
              'abilities' : 'characterbirther/choose_abilities.html',
              'circle' : 'characterbirther/choose_circle.html',
              }

NAMED_FORM_LIST = [("", CharBirthForm),
                   ("drive", DriveForm),
                   ("pillars", PillarsOfSanity),
                   ("occupation", OccupationForm),
                   ("abilities", Abilities),
                   ("circle", SourcesOfStability),
                   ]

def browse_options(request):
    # up next some logic to govern the post get methods 
    if request.method == "POST":
        form = CharBirthForm(request.POST)
        if form.is_vaild():
            return HttpResponseRedirect('/psych/')
        else:
            form = CharBirthForm()
    return render(request, 'characterbirther/make_investigator.html', DATA_ALIASES)

class BuildWizard(NamedUrlSessionWizardView):
    form_list = NAMED_FORM_LIST
    
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    
    def done(self, NAMED_FORM_LIST, **kwargs):
        return HttpResponseRedirect('/build/{}'.format(self.steps.next))

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

a line of code to filter some things out from the database        
#DriveList.objects.filter(associatedoccudrive__drive = 'Antiquarian')

'''
