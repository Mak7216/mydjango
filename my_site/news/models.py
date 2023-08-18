from django.db import models
import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name="Заголовок",max_length=50)
    body = models.TextField(verbose_name="Содержание",)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title