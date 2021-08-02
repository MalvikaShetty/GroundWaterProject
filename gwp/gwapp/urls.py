from django.urls import path
from . import views

urlpatterns = [
    path('', views.logindash, name='LoginDash'),
    path('maps/', views.loginmaps, name='LoginMaps'),
]