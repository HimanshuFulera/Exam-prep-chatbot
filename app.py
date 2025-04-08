from flask import Flask, render_template, request
import chatbot

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    flashcards = None
    error = None
    if request.method == 'POST':
        topic = request.form.get('topic')
        if topic:
            try:
                flashcards = chatbot.generate_flashcards(topic)
            except Exception as e:
                error = f"Error generating flashcards: {str(e)}"
        else:
            error = "Please enter a topic."
    return render_template('index.html', flashcards=flashcards, error=error)

# Remove app.run() - the hosting platform will handle this
