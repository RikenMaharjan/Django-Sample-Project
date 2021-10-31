from django.urls import path

from apps.blogs.views import *

urlpatterns = [
    path('create/',CreateView.as_view()),
    # View ---> setup() --> dispatch --> Determine the type of request [get, put, post, etc]

]
