from django.shortcuts import render
from django.http import HttpResponseNotFound

def successful(request):
    return HttpResponseNotFound('successful',status =200)

def created(request):
    return HttpResponseNotFound('created',status =201)

def accepted(request):
    return HttpResponseNotFound('accepted',status =202)

def non_authorization(request):
    return HttpResponseNotFound('non_authorization',status =203)

# def found(request):
#     return HttpResponseNotFound('found',status =302)

# def found(request):
#     return HttpResponseNotFound('found',status =204)

# def found(request):
#     return HttpResponseNotFound('found',status =204)





