from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect


from core.forms import SignUpForm,CreateProfileForm,ContactUsForm
from core.tokens import account_activation_token


def home(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return render(request, 'home.html', {'form': form})
    else:
        form = ContactUsForm()
    return render(request, 'home.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('core/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'core/account_activation_sent.html')

def is_employer(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['employer']
            user = request.user
            if(data == True):
                user.profile.employer = True
                user.save()
            else:
                user.profile.employer = False
                user.save()
            return HttpResponse("Hello, world. You're at the polls index.")
    else:
        form = CreateProfileForm()
    return render(request, 'core/is_employer.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        form = CreateProfileForm()
        return render(request, 'core/employer_employee.html', {'form': form})
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['employer']
            user = request.user
            if(data == True):
                user.profile.employer = True
                user.save()
            else:
                user.profile.employer = False
                user.save()
            return HttpResponseRedirect('/createprofile/employer/home/')

    else:
        return render(request, 'core/account_activation_invalid.html')

