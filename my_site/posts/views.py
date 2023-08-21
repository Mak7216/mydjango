from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Rating
from django.shortcuts import get_object_or_404
from django.template import loader
from .forms import PostForm, NewsForm

# Create your views here.
def index(request):
    template = loader.get_template("posts/index.html")
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return HttpResponse(template.render(context, request))

def detail(request, post_id):
    print(post_id)
    template = loader.get_template("posts/detail.html")
    post = get_object_or_404(Post, id=post_id)
    rate = get_object_or_404(Rating)
    context = {
        "post": post,
        "rate": rate
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template("posts/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template("posts/main.html")
    context = {}
    return HttpResponse(template.render(context, request))

def reg(request):
    template = loader.get_template("posts/reg.html")
    context = {}
    return HttpResponse(template.render(context, request))

def user(request):
    template = loader.get_template("posts/user.html")
    context = {}
    return HttpResponse(template.render(context, request))

def user_t(request):
    template = loader.get_template("posts/user_t.html")
    context = {}
    return HttpResponse(template.render(context, request))

def create_post(request):
    form = PostForm(request.POST or None)
    context = {
        "form": form
    }
    template = loader.get_template("posts/create_post.html")
    if form.is_valid():
        post = form.save()
        post.save() 
        return HttpResponseRedirect("/posts/")
    return HttpResponse(template.render(context, request))
def create_news(request):
    news = NewsForm(request.POST or None)
    context = {
        "form": news
    }
    template = loader.get_template("posts/create_news.html")
    if news.is_valid():
        post_news = news.save()
        post_news.save() 
        return HttpResponseRedirect("/news/")
    return HttpResponse(template.render(context, request))

#def posts(request):
#    template = loader.get_template("posts/login.html")
#    context = {}
#    return HttpResponse(template.render(context, request))