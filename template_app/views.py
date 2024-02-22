from django.shortcuts import render

def render_temp1(request):
     return render(request, "index.html")

def portfolio_list(request):
     portfolio = [
          {'id':1,'name':'Portfolio 1','description':'This is the description of portfolio 1','owner':'Nikhil'},    
          {'id':1,'name':'Portfolio 1','description':'This is the description of portfolio 1','owner':'Nikhil'},    
          {'id':1,'name':'Portfolio 1','description':'This is the description of portfolio 1','owner':'Nikhil'},    
          {'id':1,'name':'Portfolio 1','description':'This is the description of portfolio 1','owner':'Nikhil'},    
     ]
     return render(request,'portfolio_list.html')


