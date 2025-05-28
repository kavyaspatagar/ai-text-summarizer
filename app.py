from flask import Flask, render_template, request
from transformers import pipeline

# Initialize the Flask app
app = Flask(__name__)

# Load the summarization model
summarizer = pipeline("summarization")

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        input_text = request.form['input_text']
        summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
