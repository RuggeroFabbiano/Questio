from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question, Answer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    creationDate = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    nAnswers = serializers.SerializerMethodField(read_only=True)
    hasAnswered = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
    def get_creationDate(self, instance):
        return instance.creationDate.strftime('%d %B %Y')
    def get_nAnswers(self, instance):
        return instance.answers.count()
    def get_hasAnswered(self, instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    creationDate = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    hasVoted = serializers.SerializerMethodField(read_only=True)
    questionSlug = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Answer
        exclude = ['question', 'voterList']
    def get_creationDate(self, instance):
        return instance.creationDate.strftime('%d %B %Y')
    def get_likes(self, instance):
        return instance.voterList.count()
    def get_hasVoted(self, instance):
        request = self.context.get('request')
        return instance.voterList.filter(pk=request.user.pk).exists()
    def get_questionSlug(self, instance):
        return instance.question.slug
