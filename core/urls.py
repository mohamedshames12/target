from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('register', views.register, name='register'),
    path('create-project', views.CreateProject, name='create-project'),
    path('about-us', views.aboutUs, name='about-us'),
    path('contact-us', views.ContactUs, name='contact-us'),
    path('view/<str:pk>', views.view, name='view'),
    path('platforms', views.platforms, name='platforms'),
    path('our-project', views.OurProject, name='our-project'),
    path('services', views.services, name='services'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]