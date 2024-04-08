from django.contrib import admin
from django.urls import path
from Fit_D import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact_us',views.contact_us,name="contact_us"),
    path('services',views.services,name="services"),
    path('kids',views.kids,name="kids"),
    path('s_citizen',views.s_citizen,name="s_citizen"),
    path('sum',views.sum,name="sum"),
    path('login_form',views.login_form,name="login_form"),
    path('data',views.data,name="data")

]
