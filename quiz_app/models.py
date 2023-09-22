from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=300)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return self.question