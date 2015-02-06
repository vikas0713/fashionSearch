from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')