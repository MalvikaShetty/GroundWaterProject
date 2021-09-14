from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
                         HttpResponseRedirect, HttpResponsePermanentRedirect)
# Create your views here.


def home(request):
    return render(request, 'home.html')


def maps(request):
    return render(request, 'maps.html')


def add_data(request):
    return render(request, 'add_data.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def own_data(request):
    return render(request, 'own_data.html')


def profile(request):
    return render(request, 'profile.html')


def reports(request):
    return render(request, 'reports.html')


def view_data(request):
    return render(request, 'view_data.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def start_popup(request):
    return render(request, 'start.html')
