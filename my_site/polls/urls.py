from django.urls import path
from polls.views import (
    polls, detail_polls
)

urlpatterns = [
    path('polls/', polls, name="polls"),
    path('polls/<int:poll_id>/', detail_polls, name="detail_polls"),
]