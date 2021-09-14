from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
                         HttpResponseRedirect, HttpResponsePermanentRedirect)
# Create your views here.


def logindash(request):
    return render(request, 'base.html')


def maps(request):
    return render(request, 'maps.html')


def add_data(request):
    return render(request, 'add_data.html')
