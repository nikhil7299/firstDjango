from os import name
from django.urls import path
from .views import portfolio_list, render_temp1

urlpatterns = [
    path('temp1/',render_temp1,name='temp1'),
    path('portfolio/',portfolio_list,name='portfolio')
]