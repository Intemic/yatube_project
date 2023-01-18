from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    template = 'posts/index.html'
    return HttpResponse(render(request, template)) 

def group_posts(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse('Здесь нужно забабахать какую то информацию')