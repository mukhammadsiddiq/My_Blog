from django.urls import path
from .views import HomeView, DetailView, CreateViewPage

urlpatterns = [
    path('/post/new/', CreateViewPage.as_view(), name='create_view'),
    path('', HomeView.as_view(), name='home'),
    path('/post/<int:pk>/', DetailView.as_view(), name='detail_view')
    ## the reason for writing /post/<int:pk>/, always when we create a post, python will create
    ## list number for the post
]