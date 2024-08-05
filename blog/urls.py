from django.urls import path
from .views import HomeView, DetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('/post/<int:pk>/', DetailView.as_view(), name='detail_view')
    ## the reason for writing /post/<int:pk>/, always when we create a post, python will create
    ## list number for the post
]