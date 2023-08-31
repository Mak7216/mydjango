from django.urls import path
from polls.views import (
    poll
)

urlpatterns = [
    path('poll/', poll, name="poll"),
]