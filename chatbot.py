import google.generativeai as genai
import os

# Load API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_flashcards(topic):
    # Your existing code to generate flashcards
    prompt = f"Generate 5 flashcards for the topic: {topic}. Format each as 'Ques: [question] Ans: [answer]'"
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    flashcards = response.text.split('\n')[:5]  # Adjust based on actual response format
    return flashcards