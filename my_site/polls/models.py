from django.db import models

# Create your models here.
class Poll(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    questions = models.ManyToManyField("Question", related_name="questions")

class Question(models.Model):
    question = models.CharField(max_length=100)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer = models.CharField(max_length=100)