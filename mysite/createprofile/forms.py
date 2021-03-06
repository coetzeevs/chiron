from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from createprofile.models import Employee_Profile,Employer_Profile, Document, Profile_Picture, Listing, Logo


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

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ('description', 'document', )


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile_Picture
        fields = ('description', 'photo', )

class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ('description', 'photo', )
	