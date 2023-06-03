from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Fertilizer_Amount


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
		fields = ['Date', 'Fertilizer', 'amount']
		widgets = {
            'Date': DateInput(),
        }

class DeleteFertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer_Amount
        fields = []