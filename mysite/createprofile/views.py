from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect, reverse, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from createprofile.forms import CreateProfileFromEE, CreateProfileFromER, DocumentForm, ProfilePictureForm, ListingForm, LogoForm
from core.models import Profile
from .models import Employee_Profile, Employer_Profile , Document, Profile_Picture, Logo,Listing
from django.core.files.storage import FileSystemStorage
# Create your views here.

@login_required
def index(request):

	if request.method == 'POST':
		form = CreateProfileFromEE(request.POST)
		if form.is_valid():
			name = form.save(commit=False)
			name.user = request.user
			name.save()
			return render(request, 'createprofile/employee_home.html')
	else:
		form = CreateProfileFromEE()
	return render(request, 'createprofile/index.html', {'form': form})



@login_required
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
            return render(request, 'createprofile/employee_home.html')
    else:
        try:
            u = Employee_Profile.objects.get(user=request.user)
            form = CreateProfileFromEE(initial = request.POST, instance=u) #No request.POST
        except ObjectDoesNotExist:
            form = CreateProfileFromEE(request.FILES)
    return render(request, 'createprofile/employee_edit_profile.html', {'form': form})

@login_required
def employee_home(request):
    user = Profile.objects.get(user=request.user)
    print(user.employer)
    return render(request, 'createprofile/employee_home.html')



@login_required
def employee_view_profile(request):
    u = Employee_Profile.objects.get(user=request.user)
    print(u.user)
    print(u.current_company)
    u_stats = Employee_Profile.objects.get(user=request.user)
    doc_stats = Document.objects.get(user=request.user)
    image = Profile_Picture.objects.get(user=request.user)
    print(image.photo.url)
    return render(request, 'createprofile/employee_view_profile.html', {'image': image ,'u_stats': u_stats, 'doc_stats' : doc_stats})

@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return render(request, 'createprofile/employee_home.html')
    else:
        form = DocumentForm()
        print("fuck you")
    return render(request, 'createprofile/model_form_upload.html', {'form': form})

@login_required
def photo_form_upload(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return render(request, 'createprofile/employee_home.html')
    else:
        form = ProfilePictureForm()
        print("fuck you")
    return render(request, 'createprofile/model_form_upload.html', {'form': form})


@login_required
def emplyer_create_profile(request):
    user = Profile.objects.get(user=request.user)
    if(user.employer == False):
        return HttpResponseRedirect('/createprofile/employee/home/')
    if request.method == 'POST':
        form = CreateProfileFromER(request.POST)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return render(request, 'createprofile/employer_home.html')
    else:
        form = CreateProfileFromER()
    return render(request, 'createprofile/emplyer_create_profile.html', {'form': form})


@login_required
def emplyer_edit_profile(request):
    user = Profile.objects.get(user=request.user)
    if(user.employer == False):
        return HttpResponseRedirect('/createprofile/employee/home/')
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
            return render(request, 'createprofile/employer_home.html')
    else:
        try:
            u = Employer_Profile.objects.get(user=request.user)
            form = CreateProfileFromER(initial = request.POST, instance=u) #No request.POST
        except ObjectDoesNotExist:
            form = CreateProfileFromER(request.FILES)
    return render(request, 'createprofile/emplyer_edit_profile.html', {'form': form})

@login_required
def employer_home(request):
    user = Profile.objects.get(user=request.user)
    if(user.employer == False):
        return HttpResponseRedirect('/createprofile/employee/home/')
    return render(request, 'createprofile/employer_home.html')


@login_required
def listing_form_upload(request):
    user = Profile.objects.get(user=request.user)
    if(user.employer == False):
        return HttpResponseRedirect('/createprofile/employee/home/')
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return render(request, 'createprofile/employer_home.html')
    else:
        form = ListingForm()
        print("fuck you")
    return render(request, 'createprofile/listing_form_upload.html', {'form': form})

@login_required
def employer_photo_form_upload(request):
    user = Profile.objects.get(user=request.user)
    if(user.employer == False):
        return HttpResponseRedirect('/createprofile/employee/home/')
    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.save(commit=False)
            name.user = request.user
            name.save()
            return render(request, 'createprofile/employer_home.html')
    else:
        form = ProfilePictureForm()
        print("fuck you")
    return render(request, 'createprofile/model_form_upload.html', {'form': form})

@login_required
def employer_view_profile(request):
    user = Profile.objects.get(user=request.user)
    if(user.employer == False):
        return HttpResponseRedirect('/createprofile/employee/home/')
    u_stats = Employer_Profile.objects.get(user=request.user)
    print(u_stats.company)
    print(u_stats.user)
    print(1)
    doc_stats = Listing.objects.filter(user=request.user)
    print(2)
    image = Logo.objects.get(user=request.user)
    return render(request, 'createprofile/employer_view_profile.html', {'image': image ,'u_stats': u_stats, 'doc_stats' : doc_stats})
