from django.shortcuts import render, get_object_or_404,redirect, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from createprofile.forms import CreateProfileFromEE, CreateProfileFromER
from .models import Employee_Profile, Employer_Profile 
# Create your views here.


def index(request):

	if request.method == 'POST':
		form = CreateProfileFromEE(request.POST)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = request.user
			name.save()
			return HttpResponse("Made it")
	else:
		form = CreateProfileFromEE()
	return render(request, 'createprofile/index.html', {'form': form})

def emplyer_create_profile(request):

	if request.method == 'POST':
		form = CreateProfileFromER(request.POST)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = request.user
			name.save()
			return HttpResponse("Made it")
	else:
		form = CreateProfileFromER()
	return render(request, 'createprofile/emplyer_create_profile.html', {'form': form})



def emplyer_edit_profile(request):
    if request.method== 'POST':
        try:
            u = Employer_Profile.objects.get(user=request.user)
            form = CreateProfileFromER(request.POST, instance=u)
        except ObjectDoesNotExist:
            form = CreateProfileFromER(request.POST, request.FILES)
        if form.is_valid():  #is_valid is function not property
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponse("Made it")
    else:
        try:
            u = Employer_Profile.objects.get(user=request.user)
            form = CreateProfileFromER(initial = request.POST, instance=u) #No request.POST
        except ObjectDoesNotExist:
            form = CreateProfileFromER(request.FILES)
    return render(request, 'createprofile/emplyer_edit_profile.html', {'form': form})

def emplyee_edit_profile(request):
    if request.method== 'POST':
        try:
            u = Employee_Profile.objects.get(user=request.user)
            form = CreateProfileFromEE(request.POST, instance=u)
        except ObjectDoesNotExist:
            form = CreateProfileFromEE(request.POST, request.FILES)
        if form.is_valid():  #is_valid is function not property
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return HttpResponse("Made it")
    else:
        try:
            u = Employee_Profile.objects.get(user=request.user)
            form = CreateProfileFromEE(initial = request.POST, instance=u) #No request.POST
        except ObjectDoesNotExist:
            form = CreateProfileFromEE(request.FILES)
    return render(request, 'createprofile/employee_edit_profile.html', {'form': form})

def employee_home(request):
    return render(request, 'createprofile/employee_home.html')

def employee_view_profile(request):
    u = Employee_Profile.objects.get(user=request.user)
    print(u.user)
    print(u.current_company)
    return render(request, 'createprofile/employee_view_profile.html', {'u':u})





