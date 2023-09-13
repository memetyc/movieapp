
from django.urls import path
from .views import *

urlpatterns = [
    path('login',login_request,name='login'),
    path('register',register_request,name='register'),
    path('loguot',logut_request,name='logout'),
    path('change_password',change_password,name='change_password'),
    path('profile',profile,name='profile'),
    path('watch_list',watch_list,name='watch_list'),
]
