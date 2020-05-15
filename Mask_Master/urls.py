"""Mask_Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^index',index,name="index"),                          #home page
    url(r'^logout',logout,name="logout"),                       #logout
    url(r'^signin',signin,name="signin"),                       #sign in page
    url(r'^signup',signup,name="signup"),                       #sign up page
    url(r'^customer',customer,name="customer"),                 #user registration
    url(r'^maker_reg',maker_reg,name="maker_reg"),              #maker register page
    url(r'^reg_maker',reg_maker,name="reg_maker"),              #maker registartion
    url(r'^ck_login',ck_login,name="ck_login"),                 #login check

    
    #-----------------user-------------------------------------------------------
    
    url(r'^u_home',u_home,name="u_home"),                       #user home
    url(r'^prof_user',prof_user,name="prof_user"),              #edit profile
    url(r'^update_prof',update_prof,name="update_prof"),        #update profile
    url(r'^orders',orders,name="orders"),                       #order track
    url(r'^track',track,name="track"),                          #order track
    

    #-----------------------maker--------------------------------------------------

    url(r'^prd_home',prd_home,name="prd_home"),                 #maker home
    url(r'^mkr_prf',mkr_prf,name="mkr_prf"),                    #edit profile
    url(r'^ipmkr_prof',ipmkr_prof,name="ipmkr_prof"),           #update profile
    url(r'^vw_stock',vw_stock,name="vw_stock"),                 #stock view
    url(r'^ad_stock',ad_stock,name="ad_stock"),                 #add stock
    url(r'^lv_stock',lv_stock,name="lv_stock"),                 #update stock
    
]
