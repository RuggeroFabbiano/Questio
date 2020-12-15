"""
Serializers for SPA app.
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Question, Answer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user object
    """
    class Meta:
        model = User
        fields = ["username"]

class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer of question object
    """
    author = serializers.StringRelatedField(read_only=True)
    creationDate = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    nAnswers = serializers.SerializerMethodField(read_only=True)
    hasAnswered = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
    def get_creation_date(instance):
        """
        get creation date attribute
        """
        return instance.creation_date.strftime('%d %B %Y')
    def get_n_answers(self, instance):
        """
        get number of answer instances
        """
        return instance.answers.count()
    def get_has_answered(self, instance):
        """
        flag on if user has already answered
        """
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()

class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for answer object
    """
    author = serializers.StringRelatedField(read_only=True)
    creation_date = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    has_voted = serializers.SerializerMethodField(read_only=True)
    question_slug = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Answer
        exclude = ['question', 'voterList']
    def get_creation_date(self, instance):
        """
        get creation date attribute
        """
        return instance.creation_date.strftime('%d %B %Y')
    def get_likes(self, instance):
        """
        get number of likes
        """
        return instance.voterList.count()
    def get_has_voted(self, instance):
        """
        flag on if user has already voted
        """
        request = self.context.get('request')
        return instance.voter_list.filter(pk=request.user.pk).exists()
    def get_question_slug(self, instance):
        """
        get unique slug for question URL
        """
        return instance.question.slug
