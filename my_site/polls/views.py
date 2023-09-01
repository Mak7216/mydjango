from django.shortcuts import render
from .models import Poll, Answer, Question
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def polls(request):
    template = loader.get_template("posts/polls.html")
    polls = Poll.objects.all()
    context = {
        "polls": polls,
    }
    return HttpResponse(template.render(context, request))

def detail_polls(request, poll_id):
    template = loader.get_template("posts/detail_poll.html")
    poll = Poll.objects.get(id=poll_id)
    questions = poll.questions.all()
    context = {
        "poll": poll,
        "questions": questions
    }
    return HttpResponse(template.render(context, request))