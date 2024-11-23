from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def abdullah (request):
    return HttpResponse ('welcomne to django')