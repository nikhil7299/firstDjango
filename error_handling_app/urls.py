from django.urls import path
from os import name
from .import views


# urlpatterns = [
#     path('successful/',views.successful,name='successful'),
#     path('created/',views.created,name='created'),
#     path('accepted/',views.accepted,name='accepted'),
#     path('non-authorization-info/',views.non_authorization_info,name='non_authorization_info'),
#     path('found/',views.found,name='found'),
#     path('bad-request/',views.bad_request,name='bad_request'),
#     path('unauthorized/',views.unauthorized,name='unauthorized'),
#     path('payment-required/',views.payment_required,name='payment_required'),
#     path('forbidden/',views.forbidden,name='forbidden'),
#     path('not-found/',views.not_found,name='not_found'),
#     path('conflict/',views.conflict,name='conflict'),
#     path('url-too-long/',views.url_too_long,name='url_too_long'),
#     path('request-timeout/',views.request_timeout,name='request_timeout'),
#     path('internal-server-error/',views.internal_server_error,name='internal_server_error'),
#     path('bad-gateway/',views.bad_gateway,name='bad_gateway'),
#     path('service-unavailable/',views.service_unavailable,name='service_unavailable'),
#     path('http-version-not-supported/',views.http_version_not_supported,name='http_version_not_supported'),
#     path('loop-detected/',views.loop_detected,name='loop_detected'),
# ]