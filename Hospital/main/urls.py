from django.urls import path
from . import views


app_name = "main"

urlpatterns = [

    path('', views.index_page, name="index_page"),
    path('contact/', views.contact_me, name="contact"),
    path('about/', views.about, name="about"),
    path('details/', views.details, name="details"),
    path('clinic/', views.clinic, name="clinic"),
    path('doctors/', views.doctors, name="doctors"),
    path("add/", views.add_clinic, name="addclinic"),
    

  
]