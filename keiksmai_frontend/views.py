from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

def index(request):
	return render(request, 'keiksmai_frontend/index.html')
