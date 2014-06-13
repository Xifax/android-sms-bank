from django.shortcuts import render

from utils.scanner import Scanner
from utils.sms import Sms

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
        'grunts.html',
        {'grunts': Scanner().scan()}
    )


def grunt(request, grunt):
    """Display device sms list and controls"""
    return render(
        request,
        'grunt.html',
        {'grunt': grunt, 'sms_sent': Sms(grunt).list()}
    )


##############
# Additional #
##############


def info(request):
    """Display application info"""
    return render(request, 'about.html')
