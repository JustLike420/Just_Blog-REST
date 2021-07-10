from django.contrib import admin
from django.urls import path


from .views import *

urlpatterns = [
    path('post/', PostListView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view()),
    path('comment/', CommentCreateView.as_view()),
]