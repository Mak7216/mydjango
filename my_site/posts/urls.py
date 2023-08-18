from django.urls import path
from posts.views import (
    index, main, login, reg, user, user_t, detail, create_post, create_news
)

urlpatterns = [
    path('', main),
    path('login/', login),
    path('register/', reg),
    path('users/', user),
    path('u/test/', user_t),
    path('posts/', index),
    path('posts/<int:post_id>/', detail),
    path('create_post/', create_post),
    path('create_news/', create_news),
]