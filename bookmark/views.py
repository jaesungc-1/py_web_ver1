from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark    #리스트를 보여줄 모델

class BookmarkDV(DetailView):
    model = Bookmark