"""
Model definition for SPA app.
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Profile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Question(models.Model):
    """
    Question model
    """
    content = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

class Answer(models.Model):
    """
    Answer model
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    voter_list = models.ManyToManyField(User, related_name="voters")
