from django.urls import path
from os import name
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('books/',views.books,name='books'),
]