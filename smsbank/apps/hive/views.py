# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import(
    login as login_user,
    logout as logout_user,
    authenticate
)

from utils.scanner import Scanner
from utils.sms import Sms

from forms import SMSForm, CustomAuthForm, CustomRegisterForm
from models import Profile, Device

################
# Landing page #
################


def index(request):
    """Display landing page"""
    return render(request, 'home.html')


def login(request):
    """Login existing user and redirect to device list page"""

    if request.user.is_authenticated():
        return redirect('grunts')

    if request.method == 'POST':
        form = CustomAuthForm(data=request.POST)
        if not form.is_valid():
            return render(
                request,
                'auth/login.html',
                {'form': form}
            )

        # If form is valid, try to authenticate user
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            # Log in and redirect to device list
            login_user(request, user)
            return redirect('grunts')
        else:
            return render(
                request,
                'auth/login.html',
                {'form': form}
            )
    else:
        form = CustomAuthForm()

    return render(request, 'auth/login.html', {'form': form})


def register(request):
    """Try to register new user"""

    if request.user.is_authenticated():
        return redirect('grunts')

    if request.method == 'POST':
        form = CustomRegisterForm(data=request.POST)
        if not form.is_valid():
            return render(
                request,
                'auth/register.html',
                {'form': form}
            )
        else:
            # If valid form -> create user
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            # And associate profile
            profile = Profile()
            profile.user = user
            profile.save()

            # Login registered user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login_user(request, user)

            # Go to device list
            return redirect('grunts')
    else:
        form = CustomRegisterForm()

    return render(request, 'auth/register.html', {'form': form})

#####################
# Working with hive #
#####################


def grunts(request):
    """Display device list"""

    if not request.user.is_authenticated():
        return redirect('index')

    # Get device list available for this user
    try:
        profile = request.user.profile.get()
        devices = profile.devices.all()

    # If admin, re-scan device list
    except Profile.DoesNotExist:
        devices = Device.objects.all()
        if not devices:
            Scanner().scan(persist=True)
            devices = Device.objects.all()

    return render(
        request,
        'devices/grunts.html',
        {'grunts': devices}
    )


def grunt_list(request, grunt):
    """Display device sms list and controls"""

    if not request.user.is_authenticated():
        return redirect('index')

    return render(
        request,
        'devices/grunt.html',
        {'grunt': grunt, 'sms_sent': Sms(grunt).list()}
    )


def grunt_send(request, grunt):
    """Send SMS via specified grunt"""

    if not request.user.is_authenticated():
        return redirect('index')

    sms_sent = False
    error_message = False

    if request.method == 'POST':
        form = SMSForm(data=request.POST)
        if form.is_valid():
            sms_sent = Sms(grunt).send(
                form.cleaned_data['phone'],
                form.cleaned_data['message'],
            )
        else:
            error_message = u'Указаны неверные данные'
    else:
        form = SMSForm()

    return render(request, 'devices/sms-send.html', {
        'grunt': grunt,
        'form': form,
        'sms_sent': sms_sent,
        'error_message': error_message,
    })


def logout(request):
    """Try to logout existing user"""
    if request.user.is_authenticated():
        logout_user(request)
        return redirect('index')


##############
# Additional #
##############


def info(request):
    """Display application info"""
    return render(request, 'about.html')
