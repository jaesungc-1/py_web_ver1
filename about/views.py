from django.shortcuts import render
from django.views.generic import ListView
from about.models import About

# Create your views here.

class AboutLV(ListView):
    model = About