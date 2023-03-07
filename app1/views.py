from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def rel(request):
    return HttpResponse('this is first project in app1')


def sam(request):
    return HttpResponse('<h1>this is second project in app1</h1>')