from django.urls import path
from User_App import views

urlpatterns = [
    path('', views.index),
    path('profile/', views.profile, name='profile'),
    path('notes/', views.notes, name='notes'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('otpverify/', views.otpverify, name='otpverify'),
    path('user_settings/', views.user_settings, name='user_settings'),

]
