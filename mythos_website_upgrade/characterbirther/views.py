from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView

#gotta import the ManagementForm to be able to redefine the get_context_data for the wiazard view
from formtools.wizard.views import NamedUrlSessionWizardView, ManagementForm

#models and forms used in this view
from birthcharacter.models import OccupationList, AbilityList, DriveList, AssociatedOccuAbil, AssociatedOccuDrive
from characterbirther.models import BirthForm
from characterbirther.forms import CharBirthForm, PillarsOfSanity, Abilities, SourcesOfStability

#for passing character options data from the models
DATA_ALIASES = {'occupations' : OccupationList.objects.all().order_by('occupation'),
                'abilities' : AbilityList.objects.all().order_by('ability'),
                'I_abilities' : AbilityList.objects.filter(major_type='I').order_by('ability'),
                'G_abilities' : AbilityList.objects.filter(major_type='G').order_by('ability'),
                'drives' : DriveList.objects.all().order_by('drive'),
                'recommended_occupations' : AssociatedOccuAbil.objects.all(),
                }

#for rendering each wizard form in a different template
TEMPLATES =  {'start' : 'characterbirther/choose_base.html',
              'drive' : 'characterbirther/choose_psych.html',
              'pillars' : 'characterbirther/choose_pillars.html',
              'occupation' : 'characterbirther/choose_occupations.html',
              'abilities' : 'characterbirther/choose_abilities.html',
              'circle' : 'characterbirther/choose_circle.html',
#              'confirm' : 'characterbirther/character_confirm.html'
                }

#different fields for the different templates to render of CharBirthForm
DISPLAY_LISTS =  {'start' : ['name', 'pronoun', 'age', 'birthplace'],
                  'drive' : ['drive'],
#                  'pillars' : 'characterbirther/choose_pillars.html',
                  'occupation' : ['occupation'],
#                  'abilities' : 'characterbirther/choose_abilities.html',
#                  'circle' : 'characterbirther/choose_circle.html',
#                  'confirm' : 'characterbirther/character_confirm.html'
                  }

#the progression for the wizard
NAMED_FORM_LIST = [("start", CharBirthForm),
                   ("drive", CharBirthForm),
                   ("pillars", PillarsOfSanity),
                   ("occupation", CharBirthForm),
                   ("abilities", Abilities),
                   ("circle", SourcesOfStability),
                   ]

'''
#a list of things form some reason at some point in my sortid django learning process
HIDDEN_INITIAL_FLAG =  {
    'start' : {'confirm_start' : True},
    'drive' : {'confirm_drive' : True},
    'pillars' : {'confirm_pillars' : True},
    'occupation' : {'confirm_occupation' : True},
    'abilities' : {'confirm_abilities' : True},
    'circle' : {'confirm_circle' : True},
    }
'''

'''
#browse options and create a character
def browse_options(request):
    form = CharBirthForm()
    return render(request,'characterbirther/make_investigator.html', DATA_ALIASES)
'''

class BuildWizard(NamedUrlSessionWizardView):
    form_list = NAMED_FORM_LIST
#    initial_dict = HIDDEN_INITIAL_FLAG

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

        #pass character option contexts only when needed, in the future make this more specific, also update the BirthForm derived forms with the display fields for the different wizard renderings
        if context['step'] == 'pillars':
            return context
        elif context['step'] == 'circle':
            return context
        else:
            context.update(DATA_ALIASES)
            if context['step'] == 'start':
                context.update({'display_start' : DISPLAY_LISTS['start']})
                return context
            elif context['step'] == 'drive':
                context.update({'display_drive' : DISPLAY_LISTS['drive']})
                return context
            elif context['step'] == 'occupation':
                context.update({'display_occupation' : DISPLAY_LISTS['occupation']})
                #return context
            else:
                return context
                
    #to render a different template for different pieces of each form
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    #to save the form and specify the done state
    def done(self, form_list, form_dict, **kwargs):
        #debug
        import pdb, pprint; pdb.set_trace()
        birthcharacter = BirthForm.save(commit=False)
        for form, instance in form_dict.items():
            print(instance)
            return birthcharacter
        birthcharacter.save()
        return HttpResponseRedirect(self.request, 'test_result')

#the finished character view displays all the characters choices for a final one page editing
def finished_character(request):
    form = CharBirthForm(request.POST)
    return render(request, 'characterbirther/make_investigator.html', {'abilities' : Abilities})

'''
junk code
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

    #to process the form data between each step add flags as a dict to data for completion
    def get_form_step_data(self, form):
        confirm_step = 'confirm_' + form.data['build_wizard-current_step']
        form = form.data.update({confirm_step : True})
        return form.data
'''
