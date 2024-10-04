import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
# Configure the API key from environment variables
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Function to generate flashcards using Gemini AI
def generate_flashcards(input_text):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Create the model for generating flashcards
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction= "You are an AI assistant helping students study for their university classes. I need you to generate flashcards based on the class or topic provided. Each flashcard should contain a question and a corresponding answer. The questions should cover important concepts, key facts, or common exam questions related to the class or topic. Provide concise and clear answers for each question.\n\nFormat each flashcard in the following format:\n- Question: [Insert question here]\n- Answer: [Insert answer here]\n\nPlease generate 5-10 flashcards for the following:\n\nClass: {class_name}\nTopic: {topic_name}\n\nIf no specific topic is provided, generate flashcards that cover a wide range of key concepts from the entire class."
    )

    # Start a new chat session
    chat_session = model.start_chat(history=[])

    # Send the user's input text (class or topic) to the model
    response = chat_session.send_message(input_text)

    # Assuming the response contains the flashcards as text
    flashcards = response.text

    # You may want to parse the flashcards if necessary (e.g., split by question/answer format)
    # For simplicity, we'll return the response as is
    return parse_flashcards(flashcards)

# Helper function to parse flashcards from the response text (adjust this as per your needs)
def parse_flashcards(flashcard_text):
    # Example: Split flashcards by newline or another delimiter if needed
    # This is just a placeholder logic
    flashcard_pairs = flashcard_text.split("\n\n")  # Assuming flashcards are separated by two newlines
    flashcards = []
    for pair in flashcard_pairs:
        if ":" in pair:
            question, answer = pair.split(":", 1)
            flashcards.append({
                "question": question.strip(),
                "answer": answer.strip()
            })
    return flashcards