from django.urls import path
from os import name
from .import views

urlpatterns = [
    path('',views.contact_form,name='contact_form'),
    # path('created/',views.created,name='created'),
    # path('accepted/',views.accepted,name='accepted'),
]