# admissions/urls.py
from django.urls import path
from admissions import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('enroll/', views.enroll_participant, name='enroll_participant'),
]
