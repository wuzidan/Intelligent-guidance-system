"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app01 import views
# from app01.views import dkt_prediction
urlpatterns = [
    path('index/', views.index,name='index'),
    path('user/list/',views.user_list),
# path('dkt_prediction/', views.dkt_prediction),
path('tpl/',views.tpl),
path('user/add/',views.user_add),
path('test/',views.test),
path('update_aigroup/', views.update_aigroup_percent, name='update_aigroup_percent'),
path('login/',views.login),
 path('challenge/<int:item_id>/', views.challenge_detail, name='challenge_detail'),
]
