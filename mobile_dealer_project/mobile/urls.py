# mobile/urls.py

from django.urls import path
from .views import mobile_list, add_mobile, buy_mobile

urlpatterns = [
    path('', mobile_list, name='mobile_list'),
    path('add/', add_mobile, name='add_mobile'),
    path('buy/', buy_mobile, name='buy_mobile'),
]
