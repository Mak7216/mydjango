from django.db import models

# Create your models here.
class Poll(models.Model):
    upload_img = models.FileField(upload_to="./uploads/polls/imgs/%Y/%m/%d/", verbose_name="Добавить опрос", null=True)
    
    def __str__(self) -> str:
        return self.title