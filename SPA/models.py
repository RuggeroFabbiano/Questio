from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Question(models.Model):
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    creationDate = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)
    voterList = models.ManyToManyField(User, related_name="voters")
