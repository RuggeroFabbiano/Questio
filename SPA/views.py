"""
Views for SPA app.
"""

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Answer
from .permissions import ReadOnlyOrIsAuthor
from .serializers import AnswerSerializer, QuestionSerializer, UserSerializer

class SPAView(LoginRequiredMixin, TemplateView):
    """
    Main single-page-application view
    """
    if settings.DEBUG:
        template_name = "SPA_debug.html"
    else:
        template_name = 'SPA.html'

class GetUser(APIView):
    """
    API view to get user
    """
    def get(self, request):
        """
        GET method
        """
        return Response(UserSerializer(request.user).data)

class QuestionView(viewsets.ModelViewSet):
    """
    View for question list
    """
    queryset = Question.objects.all().order_by('-creationDate')
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrIsAuthor]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AnswerView(generics.CreateAPIView):
    """
    API view for user's answer to given question
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    def perform_create(self, serializer):
        related_question = get_object_or_404(Question,
                                             slug=self.kwargs.get('slug'))
        if related_question.answers.filter(author=self.request.user).exists():
            raise ValidationError("You've already answered this question")
        serializer.save(author=self.request.user, question=related_question)

class QuestionAnswersView(generics.ListAPIView):
    """
    API view for question's answers
    """
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrIsAuthor]
    def get_queryset(self):
        filt_obj = Answer.objects.filter(question__slug=self.kwargs.get('slug'))
        return filt_obj.order_by('-creationDate')

class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to get question details
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrIsAuthor]

class AnswerLikeView(APIView):
    """
    API view to get answer's likes
    """
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        """
        POST method
        """
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voterList.add(user)
        answer.save()
        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, pk):
        """
        Delete answer
        """
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voterList.remove(user)
        answer.save()
        serializer_context = {'request': request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
