from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Fertilizer_Amount, Fertilizer_Cost, Fertilizer_Price
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
	Amount = forms.DecimalField(required=True,label= "amount", widget=forms.NumberInput(attrs={'placeholder': 0}))
	class Meta:
		model = Fertilizer_Amount
		model2 = Fertilizer_Cost
		fields = ['Date', 'H2O_m3_Per_Ha', 'UV_percent', 'Injection_Ratio','Fertilizer',
	     'Amount', 'Media','Area_Ha']
		widgets = {
            'Date': DateInput(),
	    
        }

class Fertilizer_PricesForm(forms.ModelForm):
	# specify the name of model to use
	price_Usd = forms.DecimalField(required=True,label= "price_Usd", widget=forms.NumberInput(attrs={'placeholder': 0}))
	class Meta:
		model = Fertilizer_Price
		fields = ['Date', 'Fertilizer', 'price_Usd']
		widgets = {
			'Date': DateInput(),
			
		}


class DeleteFertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer_Amount
        fields = []