from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=50)
    body = models.TextField(verbose_name="Содержание",max_length=500)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.title


class SubPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    minitext = models.TextField()

"""
Д/з 
1 улучшить модель для новостей (в новостях должны быть картинка и видео)
2 улучшить модель для постов (должна быть картинка и .pdf файл)
3 Создать подель рейтинга постов
4 реорганизовать все .html шаблоны и переместить все стили в один файл
5 продолжать писать про sql
6 коды состояния http понимать
7 протокол tcp/ip
"""