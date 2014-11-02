from django.forms import ModelChoiceField, Form
from .models import PrecinctArea, Precinct

class PrecinctSelectForm(Form):

	precint_area = ModelChoiceField(queryset=PrecinctArea.objects.all(),label="Township/City")
	precinct = ModelChoiceField(queryset=Precinct.objects.all())
