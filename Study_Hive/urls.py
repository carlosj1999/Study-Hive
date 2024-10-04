from django.contrib import admin
from django.urls import path, include
from flashcard import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flashcard/', include('flashcard.urls')),  # Add this line
]