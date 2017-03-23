from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Profile, ContactUs


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('first_name','last_name','username', 'email', 'password1', 'password2', )


class CreateProfileForm(forms.ModelForm):
	employer = forms.BooleanField(required=False)

	class Meta:
		model = Profile
		fields = ('employer',)

class ContactUsForm(forms.ModelForm):
	surname = forms.CharField(max_length=30, required=True, help_text='Please enter your surname.')
	email = forms.EmailField(max_length=254, required=True,help_text='Please enter a valid email address.')
	subject = forms.CharField(max_length=1000, required=True, help_text='Please enter subject line.')
	email_body = forms.CharField(max_length=2000, required=True, help_text='Please enter email body.')
	phone_number = forms.CharField(required=False, help_text='Optional.')
	current_occupation = forms.CharField(max_length=500, required=False, help_text='Optional.')
	location = forms.CharField(max_length=500, required=False, help_text='Optional.')

	class Meta:
		model = ContactUs
		fields = ('surname','email','subject', 'email_body', 'phone_number', 'current_occupation', 'location',)

