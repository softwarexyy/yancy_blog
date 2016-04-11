from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Article.objects.all()   # get all objects of class Article
    return render(request, 'home.html', {'post_list':post_list})


# for every blog, how to deal with it (using id)
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'everyarticle.html', {'post':post})