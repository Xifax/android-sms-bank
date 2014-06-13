from django.conf.urls import patterns, url

# from controllers import views, api
import views

urlpatterns = patterns(
    '',
    # Landing
    url(r'^$', views.index, name='index'),
    # Device list
    url(r'^grunts/', views.grunts, name='grunts'),
    # url(r'^sms/', views.sms, name='sms'),
    # Additional
    url(r'^info/', views.info, name='info'),
    # Auth
    # url(r'^login/', views.login, name='login'),
    # url(r'^register/', views.register, name='register'),
)
