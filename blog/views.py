from django.shortcuts import render
from django.views.generic import ListView, DetailView
from.models import Post
from django.views.generic.edit import CreateView
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class DeatiledText(DetailView):
    model = Post
    template_name = 'detailed.html'


class CreateViewPage(CreateView):
    model = Post
    template_name = 'create_blog.html'
    fields = ['title', 'author', 'body']