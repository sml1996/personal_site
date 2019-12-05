from django.shortcuts import render, loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))
