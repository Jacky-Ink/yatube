from tokenize import group
from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:any_slug>/', views.group_posts, name='group_posts')
] 
