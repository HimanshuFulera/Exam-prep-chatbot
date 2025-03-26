import google.generativeai as genai
import os
import random
import time

# Load API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_flashcards(topic):
    model = genai.GenerativeModel(
        'gemini-1.5-pro',
        generation_config={
            "temperature": 1.0,  # Higher temperature for more randomness
        }
    )
    
    # Add a random number and timestamp to the prompt to ensure uniqueness
    random_seed = random.randint(1, 10000)
    timestamp = int(time.time())
    prompt = (f"Generate exactly 5 flashcards for the topic: {topic} (variation {random_seed}-{timestamp}). "
              f"Each flashcard must be formatted as 'Ques: [question] Ans: [answer]'. "
              f"Ensure there are no blank lines between flashcards.")
    
    response = model.generate_content(prompt)
    
    # Split the response into lines and filter out empty lines
    flashcards = [line.strip() for line in response.text.split('\n') if line.strip()]
    
    # If fewer than 5 flashcards, generate more with a fallback prompt
    while len(flashcards) < 5:
        remaining = 5 - len(flashcards)
        fallback_prompt = (f"Generate {remaining} more flashcards for the topic: {topic} (variation {random_seed}-{timestamp}). "
                          f"Each flashcard must be formatted as 'Ques: [question] Ans: [answer]'.")
        fallback_response = model.generate_content(fallback_prompt)
        additional_flashcards = [line.strip() for line in fallback_response.text.split('\n') if line.strip()]
        flashcards.extend(additional_flashcards)
    
    # Trim to exactly 5 flashcards
    return flashcards[:5]