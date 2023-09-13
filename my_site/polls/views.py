from django.shortcuts import render
from .models import Poll, Answer, Question
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def polls(request):
    template = loader.get_template("polls/polls.html")
    polls = Poll.objects.all()
    context = {
        "polls": polls,
    }
    return HttpResponse(template.render(context, request))

@login_required
def detail_polls(request, poll_id):
    template = loader.get_template("polls/detail_poll.html")
    poll = Poll.objects.get(id=poll_id)
    questions = poll.questions.all()
    context = {
        "poll": poll,
        "questions": questions
    }
    return HttpResponse(template.render(context, request))