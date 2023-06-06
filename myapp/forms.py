from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Fertilizer_Amount
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	

class DateInput(forms.DateInput):
    input_type = 'date'
    

# create a ModelForm
class Fertilizer_AmountForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Fertilizer_Amount
		fields = ['Date', 'Water_Volume_m3', 'UV_percent', 'Injection_Ratio','Fertilizer',
	     'amount', 'Media']
		widgets = {
            'Date': DateInput(),
	    
        }
		# def __init__(self, *args, **kwargs):
		# 	super().__init__(*args, **kwargs)
		# 	self.helper = FormHelper()
		# 	self.helper.form_method = 'post'
		# 	self.helper.form_class = 'form-horizontal'
		# 	self.helper.label_class = 'col-lg-2'
		# 	self.helper.field_class = 'col-lg-8'
		# 	self.helper.form_style = 'inline'
		# 	self.helper.layout = Layout(
		# 		Row(
		# 			Column('Date', css_class='form-group col'),
		# 			Column('Media', css_class='form-group col'),
		# 			Column('Water_Volume_m3', css_class='form-group col'),
		# 			Column('UV_percent', css_class='form-group col'),
		# 			Column('Injection_Ratio', css_class='form-group col'),
		# 			Column('Fertilizer', css_class='form-group col'),
		# 			Column('amount', css_class='form-group col'),
		# 			# Column('mother_name', css_class='form-group col'),
		# 			# Column('signature_of_student', css_class='form-group col'),
		# 		)
		# 	)



class DeleteFertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer_Amount
        fields = []