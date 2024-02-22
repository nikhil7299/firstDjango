from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_user_by_id(request,user_id):
    data = {'user_id':user_id,'message':'This is sample user info by id'}
    return JsonResponse(data)

def get_user_by_name(request,user_name):
    data = {'user_name':user_name,'message':'This is sample user info by name'}
    return JsonResponse(data)

def user_profile(request,username):
    return JsonResponse({'message':f'user profile for - {username}'})