from django.forms import ModelForm, formset_factory
from .models import BirthForm, SanityPillars, InnateAbility, StabilitySources

class CharBirthForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['name', 'pronoun', 'age', 'birthplace']

class DriveForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['drive']

class SanityForm(ModelForm):
    class Meta:
        model = SanityPillars
        fields = ['pillar', 'description']
        
#formset for pillars of sanity
PillarsOfSanity = formset_factory(
    SanityForm, 
    min_num=1, 
    max_num=3, 
    can_delete=True, 
    validate_min=True, 
    validate_max=True
    )
#debug
import pdb, pprint; pdb.set_trace()

class OccupationForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['occupation']

class AbilitiesForm(ModelForm):
    class Meta:
        model = InnateAbility
        fields = ['ability', 'value']
        
#formset for abilities
Abilities = formset_factory(AbilitiesForm, can_delete=True)

class SourceBirthForm(ModelForm):
    class Meta:
        model = StabilitySources
        fields = ['name', 'relation', 'personality', 'residence']
        
#formset for sources of Stability
SourcesOfStability = formset_factory(SourceBirthForm, max_num=4, can_delete=True)
