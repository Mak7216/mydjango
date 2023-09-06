from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import News
from posts.models import Post
from django.shortcuts import get_object_or_404

# Create your views here.
"""
Сделать вывод всех новостей и вывод одной новости + templates + urls 
"""
def detail_new(request, post_id):
    print(post_id)
    template = loader.get_template("news/new.html")
    new = get_object_or_404(News, id=post_id)
    context = {
        "new": new
    }
    return HttpResponse(template.render(context, request))

def news(request):
    template = loader.get_template("main.html")
    posts = News.objects.all()
    context = {
        "posts": posts
    }
    return HttpResponse(template.render(context, request))