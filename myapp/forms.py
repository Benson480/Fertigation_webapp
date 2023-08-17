from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (Fertilizer_Amount, Fertilizer_Cost, Fertilizer_Price, Fertilizer_Element,
                      Fertilizer, UploadedImage, Fertilizer_Recycle)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from django.contrib.auth.forms import AuthenticationForm


# Create your forms here.
class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

class LoginForm(AuthenticationForm):
    # currently Not in use -- Hard to implement
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

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
    # Date = forms.DateField(input_formats=['%d-%m-%Y'])
    Observation = forms.CharField(
        required=False,
        label="Observation",
        widget=forms.Textarea(attrs={'placeholder': "", 'rows': 3, 'cols': 40}))
    Fertilizer_Amount = forms.DecimalField(required=True,label= "Fertilizer Amount", widget=forms.NumberInput(attrs={'placeholder': 0}))
    Tank_mix_Volume = forms.DecimalField(required=True,label= "Tank_mix_Volume", widget=forms.NumberInput(attrs={'placeholder': 1000}))
    class Meta:
        model = Fertilizer_Amount
        model2 = Fertilizer_Cost
        fields = ['Date', 'H2O_m3_Per_Ha', 'UV_percent', 'Tank_mix_Volume','Fertilizer',
	     'Fertilizer_Amount', 'Media','Area_Ha', 'Fertigation_line', 'Observation']
        widgets = {
            'Date': DateInput(),
	    
        }


class Fertilizer_ElementsForm(forms.ModelForm):
    # Element_1 = forms.CharField(
    #     required=True,
    #     label="",
    #     widget=forms.TextInput(attrs={'placeholder': "Element 1 *", 'style': 'width:15ch'})
    # )
    Composition_1 = forms.DecimalField(
        required=True,
        label="",
        widget=forms.NumberInput(attrs={'placeholder': "%", 'style': 'width:10ch'})
    )

    Composition_2 = forms.DecimalField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={'placeholder': "%", 'style': 'width:10ch'})
    )

    Composition_3 = forms.DecimalField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={'placeholder': "%", 'style': 'width:10ch'})
    )

    Composition_4 = forms.DecimalField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={'placeholder': "%", 'style': 'width:10ch'})
    )

    class Meta:
        model = Fertilizer_Element
        fields = [
            'Date','Fertilizer', 'Element_1', 'Composition_1', 'Element_2', 'Composition_2', 'Element_3',
            'Composition_3', 'Element_4', 'Composition_4'
        ]
        widgets = {
            'Date': DateInput(),
        }


class Fertilizer_PricesForm(forms.ModelForm):
	# specify the name of model to use
	price_Usd = forms.DecimalField(required=True,label= "price_Usd", widget=forms.NumberInput(attrs={'placeholder': 0}))
	class Meta:
		model = Fertilizer_Price
		fields = ['Date', 'Fertilizer','Unit_Of_Measure', 'price_Usd']
		widgets = {
			'Date': DateInput(),
			
		}

class Fertilizer_Form(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Fertilizer
		fields = ['Date','name', 'Supplier']
		widgets = {
			'Date': DateInput(),
			
		}

class Fertilizer_Recycle_Form(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Fertilizer_Recycle
		fields = ['Date','Uv_Element', 'Uv_PPM']
		widgets = {
			'Date': DateInput(),
			
		}               

class DeleteFertilizerForm(forms.ModelForm):
    class Meta:
        model = Fertilizer_Amount
        fields = []
	
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image', 'about_Image', 'title']