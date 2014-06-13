# coding: utf-8
from django.shortcuts import render

from utils.scanner import Scanner
from utils.sms import Sms

from forms import SMSForm

################
# Landing page #
################


def index(request):
    """Display landing page"""
    return render(request, 'home.html')

#####################
# Working with hive #
#####################


def grunts(request):
    """Display device list"""
    return render(
        request,
        'devices/grunts.html',
        {'grunts': Scanner().scan()}
    )


def grunt_list(request, grunt):
    """Display device sms list and controls"""
    return render(
        request,
        'devices/grunt.html',
        {'grunt': grunt, 'sms_sent': Sms(grunt).list()}
    )


def grunt_send(request, grunt):
    """Send SMS via specified grunt"""
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


##############
# Additional #
##############


def info(request):
    """Display application info"""
    return render(request, 'about.html')
