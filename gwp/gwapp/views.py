from django.shortcuts import render
from django.http import (HttpResponse, HttpResponseNotFound, Http404,
                         HttpResponseRedirect, HttpResponsePermanentRedirect)
# Create your views here.


def logindash(request):
    return render(request, 'base_login_dashboard.html')


def loginmaps(request):
    return render(request, 'maps.html')
