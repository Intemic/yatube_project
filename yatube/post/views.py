from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Здесь наверное нужно что показать, главная сраница же')

def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse('Здесь нужно забабахать какую то информацию')
