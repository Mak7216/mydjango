from django.shortcuts import render
from .models import Poll
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def poll(request):
    template = loader.get_template("posts/poll.html")
    context = {}
    return HttpResponse(template.render(context, request))