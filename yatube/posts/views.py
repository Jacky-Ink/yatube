from multiprocessing import context
from re import template
from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, any_slug):
    template = 'posts/group_post.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)
