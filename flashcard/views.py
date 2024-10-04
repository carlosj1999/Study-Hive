from django.shortcuts import render, redirect
from django.contrib import messages
from flashcard.forms import FlashcardForm
from .models import Flashcard
from Study_Hive.ai import generate_flashcards  

def generate_flashcards_view(request):
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            # Get the user input data
            university = form.cleaned_data['university']
            class_field = form.cleaned_data['class_field']
            topic = form.cleaned_data['topic']

            # Formulate the input text for the AI based on user input
            input_text = f"Class: {class_field}\nTopic: {topic if topic else 'General'}"

            # Call the AI to generate flashcards
            flashcards = generate_flashcards(input_text)

            # Save flashcards to the database
            for flashcard in flashcards:
                Flashcard.objects.create(
                    question=flashcard['question'],
                    answer=flashcard['answer'],
                    class_field=class_field,  # Use the user input instead of a model reference
                    topic=topic  # Optional topic field
                )

            messages.success(request, "Flashcards generated successfully!")
            return redirect('flashcard_list')

    else:
        form = FlashcardForm()

    return render(request, 'flashcard/generate_flashcards.html', {'form': form})