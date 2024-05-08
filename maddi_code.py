from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('proindex.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0.0:
            label = "Positive"
        elif sentiment < 0.0:
            label = "Negative"
        else:
            label = "Neutral"

        return render_template('proresult.html', label=label)

if __name__ == '__main__':
    app.run(debug=True)
