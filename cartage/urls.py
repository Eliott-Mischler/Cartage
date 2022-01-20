from django.urls import path

from . import views


app_name = 'cartage'
urlpatterns = [
  path('', views.index, name='home'),
  path('login/', views.login, name='login'),
  path('register/', views.register, name='register'),
  path('trips/', views.trips, name='trips'),
  path('profile/', views.profile, name='profile'),
  path('search/', views.search, name='search'),
  path('logResult/', views.landingL, name='landingL'),
  path('registerResult/', views.landingR, name='landingR' ),
  path('messages/', views.messages, name='messages'),
  path('help/', views.help, name='help')
 ]
