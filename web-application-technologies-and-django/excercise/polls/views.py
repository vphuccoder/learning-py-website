from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('polls/index.html')
    context = {}
    return HttpResponse("Hello, world. 32e0740f is the polls index.")
    return HttpResponse(template.render({}, request))
