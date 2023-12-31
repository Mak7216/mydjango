from django.urls import path
from posts.views import (
    index, main, reg, user, user_t, detail, create_post, create_news, RateView
)

urlpatterns = [
    path('', main, name="main"),
    path('register/', reg),
    path('users/', user),
    path('u/test/', user_t),
    path('posts/', index, name='index'),
    path('posts/<int:post_id>/', detail),
    path('create_post/', create_post),
    path('create_news/', create_news),
    path('rate_plus/<int:post_id>', RateView.like),
    path('rate_minus/<int:post_id>', RateView.dislike),
]