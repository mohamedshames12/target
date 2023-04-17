from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('register', views.register, name='register'),
    path('create-project', views.CreateProject, name='create-project'),
    path('platforms', views.platforms, name='platforms'),
    path('services', views.services, name='services'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]