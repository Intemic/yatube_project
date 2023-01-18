from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title
    }
    return HttpResponse(render(request, template, context))


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title
    }
    return HttpResponse(render(request, template, context))
