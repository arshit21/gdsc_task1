from django.urls import path
from .views import *

urlpatterns = [
    path('startQuiz/', start_quiz, name='start_quiz'),
    path('questions/<int:pk>', display_question, name='questions'),
    path('score/', display_score, name='final_score')
]