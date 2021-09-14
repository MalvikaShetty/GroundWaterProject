from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('maps/', views.maps, name='Maps'),
    path('add_data/', views.add_data, name='addData'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('own_data/', views.own_data, name='ownData'),
    path('profile/', views.profile, name='Profile'),
    path('reports/', views.reports, name='Reports'),
    path('view_data/', views.view_data, name='viewData'),
    path('login/', views.login, name='Login'),
    path('signup/', views.signup, name='SignUp'),
    path('start/', views.start_popup, name='Start'),
]