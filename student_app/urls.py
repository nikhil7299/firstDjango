from django.urls import path
from os import name

from student_app.views import student_list;


urlpatterns = [
    path('list/',student_list,name='student_list'),
]