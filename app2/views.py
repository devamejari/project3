from django.shortcuts import render
from django.http import HttpResponse

def realme(request):
    return HttpResponse('this is first project in app2')

def realme2 (request):
    return HttpResponse('<h1>this is second project in app2</h1> ')

