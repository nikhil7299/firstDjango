from django.urls import path, re_path
from .views import get_user_by_id, get_user_by_name, user_profile

urlpatterns = [
    # match numeric user id
    re_path(r'^user/(?P<user_id>\d+)$',get_user_by_id,name='get_user_by_id'),
    re_path(r'^user/(?P<user_name>\w+)$',get_user_by_name,name='get_user_by_name'),
    re_path(r'^profile/(?P<username>\w+)$',user_profile,name='userprofile')

]

# urlpatterns =[
#     path('',home,name='home'),
#     path('about/',about,name='about'),
#     path('contact/',contact,name='contact')


# ]