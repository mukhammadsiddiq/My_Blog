from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Post
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class DeatiledText(DetailView):
    model = Post
    template_name = 'detailed.html'