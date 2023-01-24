from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Group, Post

# Create your views here.

NUMBER_OF_RECORD_FETCH = 10


def index(request: HttpRequest) -> HttpResponse:
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_RECORD_FETCH]
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'posts': posts,
    }
    return HttpResponse(render(request, template, context))


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = 'Записки сообщества ' + group.title
    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[
        :NUMBER_OF_RECORD_FETCH
    ]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return HttpResponse(render(request, template, context))
