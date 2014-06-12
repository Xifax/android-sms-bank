from django.shortcuts import render

                               ################
                               # Landing page #
                               ################

def index(request):
    """Display landing page"""
    # if request.user.is_authenticated():
    #     return redirect('profile')

    return render(request, 'home.html')
