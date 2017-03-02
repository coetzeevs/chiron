from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.mail import EmailMessage
from django.conf import settings
from createprofile.forms import CreateProfileFromEE
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
