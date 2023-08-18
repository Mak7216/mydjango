from django.urls import path
from news.views import news, detail_new

urlpatterns = [
    path('news/', news),
    path('news/<int:post_id>/', detail_new),
]