from flask import Flask, render_template, request, jsonify
import spacy
from textblob import TextBlob
import re

# Initialize FLASK - creates a Flask app instance 
app = Flask(__name__)

# Load spaCy Model for Named Entity Recognition (NER)
# Model recognizes the following entities: PERSON, ORG, GPE, LOC, DATE, TIME, MONEY, PERCENT, FAC, LAW
nlp = spacy.load("en_core_web_sm")

# Defines a route that returns the index.html when the start page of the app is visited
@app.route('/')
def index():
    return render_template('index.html')

# Defines a route that every HTTP request to the URL /analyze is forwarded to this function; only POST allowed to send data to a server
@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']    
    doc = nlp(text)
    
    # Extract relevant Data
    customer_name = ""
    contact_info = ""
    products = []
    filtered_text = text

    # Extract Customer Name
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            customer_name = ent.text

    # Extract contact information (E-Mails with RegEx)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    contact_info = re.findall(email_pattern, text)

    # Extract product names - Since spacy does not recognize the entity PRODUCT, you can work with regex here
    known_products = ["iPhone", "MacBook Pro", "Samsung Galaxy", "MacBook Air", "Dishwasher", "Vacuum cleaner", "Coffee maker", "Safe 3000", "Mickeys Super Adventure Part I", "Mickeys Super Adventure Part II"]
    product_pattern = r"|".join([re.escape(product) for product in known_products])
    
    products = re.findall(product_pattern, text)
    
    # Sentiment analysis with TextBlob
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_color = "green"  # default color (fiendly)
    
    # TextBlob Scale for sentiment analysis = -1 very bad; 0 neutral; +1 very good
    if sentiment < -0.5:
        sentiment_color = "red"  # red for angry
    elif sentiment < 0:
        sentiment_color = "yellow"  # yellow for sad

    # 
    result = {
        "customer_name": customer_name,
        "contact_info": contact_info,
        "products": products,
        "sentiment_color": sentiment_color,
        "filtered_text": filtered_text              # Return the text
    }

    return jsonify(result)

# FLASK check - ensures that web server is only started when script is executed directly and not when it is imported as a module
if __name__ == "__main__":
    app.run(debug=True)