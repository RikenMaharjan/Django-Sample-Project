from django.urls import path

from apps.core.views import *

urlpatterns = [
    path('login/',LoginView.as_view()),
]
