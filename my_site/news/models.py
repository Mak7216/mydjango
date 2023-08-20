from django.db import models
import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=50)
    body = models.TextField(verbose_name="Содержание",)
    date = models.DateField(auto_now_add=True)
    upload_file = models.FileField(upload_to="./uploads/news/videos/%Y/%m/%d/", verbose_name="Добавить видео")
    upload_img = models.ImageField(upload_to="./uploads/news/images/%Y/%m/%d/", verbose_name="Добавить изображение")

    def __str__(self) -> str:
        return self.title