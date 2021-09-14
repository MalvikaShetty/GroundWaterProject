from django.urls import path
from . import views

urlpatterns = [
    path('', views.logindash, name='loginDash'),
    path('maps/', views.maps, name='Maps'),
    path('add_data/', views.add_data, name='addData'),
]