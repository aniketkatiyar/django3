
from django.urls import path

from web1 import views

urlpatterns = [

    path('', views.index, name='home'),

    path('about/', views.about, name='about'),

    path('services1/', views.services1, name='services'),

    path('services2/', views.services2, name='services2'),

    path('contact/', views.contact, name='contact'),

    path('blog/', views.blog, name='blog'),

    path('signup/',  views.sign_up, name='signup'),

    path('login/',  views.user_login, name='login'),

    path('profile/',  views.user_profile, name='profile'),

    path('logout/', views.user_logout, name='logout'),



]
