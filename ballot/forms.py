from django.forms import ModelChoiceField, Form, HiddenInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, ButtonHolder

from .models import PrecinctArea, Precinct

class PrecinctSelectForm(Form):

	precinct_area = ModelChoiceField(queryset=PrecinctArea.objects.all())
	precinct = ModelChoiceField(queryset=Precinct.objects.all())

	def __init__(self, *args, **kwargs):
		super(PrecinctSelectForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_id = 'id-prec-select'
	##	self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit'
		self.helper.html5_required = True
		self.helper.label_class = 'col-lg-2'
		self.helper.field_class = 'col-lg-2'
		self.helper.layout = Layout(
			Field('precinct_area',
				  label="Township/City",
				),
			Field('precinct', 
				   disabled='disabled', 
				),
			ButtonHolder(
				Submit('submit', 
					   'View Ballot', 
					   css_class='button white', 
					   disabled='disabled',
				)
			),
		)