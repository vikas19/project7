from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_function(request):
    return HttpResponse('App1')