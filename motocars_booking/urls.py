"""motocars_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from viewer.views import *
from accounts.views import SignUpView
#from django.contrib.auth import login





urlpatterns = [

    path('admin/', admin.site.urls),
    #path('login/', login, name='login'),
    path('', base, name='base'),
    path('events/', events, name='events'),
    path('racetrack/', racetrack, name='racetrack'),
    path('reservation/', reservation, name='reservation'),
    path('reservation_list/', reservation_list, name='reservation_list'),
    path('reservation_detail/', reservation_detail, name='reservation_detail'),
    # path('create_reservation/', create_reservation, name='create_reservation'),
    path('reservation_new/', reservation_new, name='reservation_new'),
    path('reservation_delete/', reservation_delete, name='reservation_delete'),
    path('reservation_user/', reservation_user, name='reservation_user'),


    path('home/', home, name='home'),



    # app accounts

    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]

