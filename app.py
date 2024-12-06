from flask import Flask, render_template, request, jsonify
import spacy
from textblob import TextBlob
import re

app = Flask(__name__)

# Load spaCy Model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']    
    doc = nlp(text)
    
    # Extract relevant Data
    customer_name = ""
    contact_info = ""
    products = []

    # Extract Customer Name
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            customer_name = ent.text

    # Extract contact information (E-Mails with RegEx)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    contact_info = re.findall(email_pattern, text)
    
    # Extract product names
    for ent in doc.ents:
        if ent.label_ == "PRODUCT":
            products.append(ent.text)
    
    # Sentiment analysis with TextBlob
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_color = "green"  # default color (fiendly)
    
    # TextBlob Scale for sentiment analysis = -1 very bad; 0 neutral; +1 very good
    if sentiment < -0.5:
        sentiment_color = "red"  # red for angry
    elif sentiment < 0:
        sentiment_color = "yellow"  # yellow for sad
    
    result = {
        "customer_name": customer_name,
        "contact_info": contact_info,
        "products": products,
        "sentiment_color": sentiment_color,
        
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)