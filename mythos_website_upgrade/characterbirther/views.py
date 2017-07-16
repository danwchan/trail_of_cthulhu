from django.shortcuts import render
from django.views.generic import DetailView, ListView

from birthcharacter.models import OccupationList, AbilityList, DriveList, AssociatedOccuAbil, AssociatedOccuDrive
from characterbirther.forms import CharBirthForm

# Create your views here.

def browse_options(request):
    # import in the data from other methods (why is this useful?)
    characteroptions = data()
    foreign_key_tables = data2()
#    form = CharBirthForm()
#    forms = data3()
    data_aliases = {'occupations' : characteroptions['occupations'],
                    'abilities' : characteroptions['abilities'],
                    'I_abilities' : characteroptions['abilities'].filter(major_type='I'),
                    'G_abilities' : characteroptions['abilities'].filter(major_type='G'),
                    'drives' : characteroptions['drives'],
                    'recommended_occupations' : foreign_key_tables['occupation2abilities'],
                    'birth_form' : CharBirthForm(),
                    }
    # up next some logic to govern the post get methods 
    if request.method == "POST":
        form = CharBirthForm(request.POST)
        if form.is_vaild():
            return HttpResponseRedirect('/success/')
        else:
            form = CharBirthForm()
    return render(request, 'characterbirther/make_investigator.html', data_aliases)

def data():
    characteroptions = {'occupations' : OccupationList.objects.all(),
                        'abilities' : AbilityList.objects.all(),
                        'drives' : DriveList.objects.all(),
                        }
    return characteroptions

def data2():
    foreign_key_tables = {'drive2occupation' : AssociatedOccuDrive.objects.all(),
                          'occupation2abilities' : AssociatedOccuAbil.objects.all(),
                          }
    return foreign_key_tables

#def data3():
#    forms = {'birth_form' : CharBirthForm(),
#             }
#    return forms

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

a line of code to filter some things out from the database        
#DriveList.objects.filter(associatedoccudrive__drive = 'Antiquarian')

'''
