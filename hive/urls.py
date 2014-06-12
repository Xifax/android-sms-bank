from django.conf.urls import patterns, url

# from controllers import views, api
import views

urlpatterns = patterns(
    '',
    # Landing
    url(r'^$', views.index, name='index'),
    # Auth
    # url(r'^login/', views.login, name='login'),
    # url(r'^register/', views.register, name='register'),
)
