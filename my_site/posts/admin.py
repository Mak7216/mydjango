from django.contrib import admin
from posts.models import Post, SubPost, Rating

# Register your models here.
admin.site.register(Post)
admin.site.register(SubPost)
admin.site.register(Rating)