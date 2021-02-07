from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("cms home")

def login(request):
    return HttpResponse('CMS Login')
