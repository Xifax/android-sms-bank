from django.shortcuts import render

from utils.scanner import Scanner

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
    grunts = Scanner().scan()
    return render(request, 'grunts.html', {'grunts': grunts})


##############
# Additional #
##############


def info(request):
    return render(request, 'about.html')
