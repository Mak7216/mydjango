from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinLengthValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=50, validators=[MinLengthValidator(0)])
    body = models.TextField(verbose_name="Содержание",max_length=1000)
    date = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to="./uploads/posts/files/%Y/%m/%d/", verbose_name="Добавить файл (.pdf)", null=True)
    upload_img = models.ImageField(upload_to="./uploads/posts/imgs/%Y/%m/%d/", verbose_name="Добавить изображение", null=True)
    
    def __str__(self) -> str:
        return self.title
    
    def clean(self) -> None:
        return super().clean()

class SubPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    minitext = models.TextField()

class Rating(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=10, null=True)

"""
Д/з от 11.09.2023
1 посмотреть что такое cookies, сессии, токены +
2 сделать @login_required на все view, кроме login +
3 выучить все команды ORM Django +
"""