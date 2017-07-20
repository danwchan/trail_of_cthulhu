from django.forms import ModelForm
from .models import BirthForm

class CharBirthForm(ModelForm):
    class Meta:
        model = BirthForm
        fields = ['name', 'pronoun', 'age', 'birthplace']
