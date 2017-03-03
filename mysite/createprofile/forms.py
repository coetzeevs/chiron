from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from createprofile.models import Employee_Profile,Employer_Profile


class CreateProfileFromEE(forms.ModelForm):

	class Meta:
		model = Employee_Profile
		fields = (
				'current_company',
				'previous_company',
				'highest_qualification', 
				'institute_hq', 
				'highschool', 
				'bio',
				'location',
				'birth_date',
				'sql', 
				'python', 
				'r', 
				'scala', 
				'julia', 
				'tableau',)

class CreateProfileFromER(forms.ModelForm):

	class Meta:
		model = Employer_Profile
		fields = (
				'company',
				'industry',
				'bio', 
				'url', )



	