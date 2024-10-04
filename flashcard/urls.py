from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_flashcards_view, name='generate_flashcards'),
]