from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=50)
    body = models.TextField(verbose_name="Содержание",max_length=500)
    date = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to="./uploads/posts/files/%Y/%m/%d/", verbose_name="Добавить файл (.pdf)", null=True)
    upload_img = models.ImageField(upload_to="./uploads/posts/imgs/%Y/%m/%d/", verbose_name="Добавить изображение", null=True)
    
    def __str__(self) -> str:
        return self.title


class SubPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    minitext = models.TextField()

class Rating(models.Model):
    rate = models.FloatField(verbose_name="Рейтинг", max_length=10)

"""
Д/з от 25.08.2023
1 создать поиск с ORM(консоль)
2 доработать rating
3 что такое DNS и как он работает(подробно)
4 дописывать SQL
"""