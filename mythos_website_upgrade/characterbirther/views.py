from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

#gotta import the ManagementForm to be able to redefine the get_context_data for the wiazard view
from formtools.wizard.views import NamedUrlSessionWizardView, ManagementForm

#models and forms used in this view
from birthcharacter.models import OccupationList, AbilityList, DriveList, AssociatedOccuAbil, AssociatedOccuDrive
from characterbirther.forms import CharBirthForm, DriveForm, PillarsOfSanity, OccupationForm, Abilities, SourcesOfStability

#for passing character options data from the models
DATA_ALIASES = {'occupations' : OccupationList.objects.all().order_by('occupation'),
                'abilities' : AbilityList.objects.all().order_by('ability'),
                'I_abilities' : AbilityList.objects.filter(major_type='I').order_by('ability'),
                'G_abilities' : AbilityList.objects.filter(major_type='G').order_by('ability'),
                'drives' : DriveList.objects.all().order_by('drive'),
                'recommended_occupations' : AssociatedOccuAbil.objects.all(),
                }

#for rendering each wizard from in a different template
TEMPLATES =  {'start' : 'characterbirther/make_investigator.html',
              'drive' : 'characterbirther/choose_psych.html',
              'pillars' : 'characterbirther/choose_pillars.html',
              'occupation' : 'characterbirther/choose_occupations.html',
              'abilities' : 'characterbirther/choose_abilities.html',
              'circle' : 'characterbirther/choose_circle.html',
#              'confirm' : 'characterbirther/character_confirm.html'
                }

#the progression for the wizard
NAMED_FORM_LIST = [("start", CharBirthForm),
                   ("drive", DriveForm),
                   ("pillars", PillarsOfSanity),
                   ("occupation", OccupationForm),
                   ("abilities", Abilities),
                   ("circle", SourcesOfStability),
                   ]

def browse_options(request):
    # up next some logic to govern the post get methods 
#    if request.method == "POST":
#        form = CharBirthForm(request.POST)
#        if form.is_vaild():
#            return HttpResponseRedirect('/psych/')
#        else:
    form = CharBirthForm()
    return render(request,'characterbirther/make_investigator.html', DATA_ALIASES)

class BuildWizard(NamedUrlSessionWizardView):
    form_list = NAMED_FORM_LIST
    
    def get_context_data(self, form, **kwargs):
        context = super(BuildWizard, self).get_context_data(form=form, **kwargs)
        context.update(self.storage.extra_data)
        context['wizard'] = {
            'form': form,
            'steps': self.steps,
            'management_form': ManagementForm(prefix=self.prefix, initial={
                'current_step': self.steps.current,
            }),
        }
        #pass character option contexts only when needed, in the future make this more specific
        if context['step'] == 'pillars':
            return context
        elif context['step'] == 'circle':
            return context
        else:
            context.update(DATA_ALIASES)
            return context
    
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
    
    def done(self, NAMED_FORM_LIST, **kwargs):
#debug
        import pdb, pprint; pdb.set_trace()

        return HttpResponseRedirect(self.request, '/character/{}'.format(CharBirthForm(self.request.POST).data['birthcode']))
#        return HttpResponseRedirect('/build/{}'.format(self.steps.next))

#the finished character view displays all the characters choices for a final one page editing
def finished_character(request):
    form = CharBirthForm(request.POST)
    return render(request, 'characterbirther/make_investigator.html', {'abilities' : Abilities})

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
