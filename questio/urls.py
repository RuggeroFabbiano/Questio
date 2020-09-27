"""Questio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django_registration.backends.one_step.views import RegistrationView
from rest_framework.routers import DefaultRouter
from SPA import views

router = DefaultRouter()
router.register("questions", views.QuestionView)

urlpatterns = [
    # Web application authorisations
    path("accounts/sign_up", RegistrationView.as_view(success_url="/"), name="sign up"), # registration
    # path("accounts",  include('django_registration.backends.one_step.urls')), # seems useless
    path("accounts/", include('django.contrib.auth.urls')), # authentication
    # API authorisations
    path("API/accounts/register", include('rest_auth.registration.urls')), # ReST registration
    path("API/accounts/", include('rest_framework.urls')), # browsable API authentication
    path("API/accounts/ReST/", include('rest_auth.urls')), # ReST authentication
    path('API/user', views.GetUser.as_view(), name="getUser"),
    # API end-points
    path("API/", include(router.urls)),
    path("API/question/<slug:slug>/answer/", views.AnswerView.as_view(), name="answer"),
    path("API/question/<slug:slug>/answers/", views.QuestionAnswersView.as_view(), name="questionAnswers"),
    path("API/answers/<int:pk>", views.AnswerDetailView.as_view(), name="answer detail"),
    path("API/answers/<int:pk>/like", views.AnswerLikeView.as_view(), name="answer like"),
    # Administration
    path('admin/', admin.site.urls),
    # Static files
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}),
    # SPA
    re_path(".*", views.SPAView.as_view(), name="SPAView")
]
