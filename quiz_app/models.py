from django.db import models

class Questions(models.Model):
    questionNumber = models.IntegerField(unique=True)
    question = models.TextField()
    answer = models.BooleanField()