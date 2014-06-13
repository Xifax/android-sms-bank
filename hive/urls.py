from django.conf.urls import patterns, url

# from controllers import views, api
import views

urlpatterns = patterns(
    '',
    # Landing
    url(r'^$', views.index, name='index'),

    # Working with devices
    url(r'^grunts/', views.grunts, name='grunts'),
    url(r'^grunt/(?P<grunt>[a-zA-Z0-9.]+)/', views.grunt, name='grunt'),
    url(r'^send-sms/(?P<grunt>[a-zA-Z0-9.]+)/', views.send_sms, name='send-sms'),
    # url(r'^sms/', views.sms, name='sms'),

    # Additional
    url(r'^info/', views.info, name='info'),

    # Auth
    # url(r'^login/', views.login, name='login'),
    # url(r'^register/', views.register, name='register'),
)
