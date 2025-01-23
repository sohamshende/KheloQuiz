from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.TextField()
    topic = models.TextField()
    noOfQuestions = models.TextField()