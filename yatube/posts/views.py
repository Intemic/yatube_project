from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBER_OF_RECORD_FETCH = 10


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.select_related('author', 'group').all()[
        :NUMBER_OF_RECORD_FETCH
    ]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[
        :NUMBER_OF_RECORD_FETCH
    ]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
