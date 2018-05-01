from django.forms import ModelForm, inlineformset_factory, HiddenInput, ModelChoiceField
from .models import BirthForm, SanityPillars, InnateAbility, StabilitySources

class CharBirthForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['name', 'pronoun', 'age', 'birthplace', 'drive', 'occupation']

'''
#(1) no from previous mistake where each thing  was it' own form  instead of a single super big form
class CharBirthForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['name', 'pronoun', 'age', 'birthplace']
#        widgets = {'birthcode' : HiddenInput()}
#        widgets = {'confirm_start' : HiddenInput()}

class DriveForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['drive']
#        widgets = {'confirm_drive' : HiddenInput()}


class OccupationForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['occupation']
#        widgets = {'confirm_occupation' : HiddenInput()}

#(2) no longer need to define the modelform explicitly, it's made from the inlineformset_factory 

class SanityForm(ModelForm):
    class Meta:
        model = SanityPillars
        fields = ['pillar', 'description']

#commenting out the confirm fields!
#        def __init__(self, *args, **kwargs):
#            super(DocumentForm, self).__init__(*args, **kwargs)
#            self.fields['confirm_pillars'] = BooleanField(queryset=BirthForm.objects['confirm_pillars'])
#            self.fields['FORCE_confirm_pillars'] = True

#        widgets = {'confirm_pillars' : HiddenInput()}

class AbilitiesForm(ModelForm):
    class Meta:
        model = InnateAbility
        fields = ['ability', 'value']

class SourceBirthForm(ModelForm):
    class Meta:
        model = StabilitySources
        fields = ['name', 'relation', 'personality', 'residence']
'''

#formset for pillars of sanity
PillarsOfSanity = inlineformset_factory(
    BirthForm,
    SanityPillars, 
    fields = ['pillar', 'description'],
    extra = 0,
    min_num = 1, 
    max_num = 3, 
    can_delete = True, 
    validate_min = True, 
    validate_max = True,
    )

#formset for abilities
Abilities = inlineformset_factory(
    BirthForm,
    InnateAbility,
    fields = ['ability', 'value'],
    can_delete=True,
    )

#formset for sources of Stability
SourcesOfStability = inlineformset_factory(
    BirthForm,
    StabilitySources,
    fields = ['name', 'relation', 'personality', 'residence'],
    extra = 0,
    min_num = 1,
    max_num = 4,
    can_delete = True,
    validate_min = True, 
    validate_max = True,
    )
