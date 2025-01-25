from flask import Flask, render_template, request 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
from recommendations import StressRecommendations

app = Flask(__name__)

# Initialize the recommendation system
recommender = StressRecommendations()

# Load the trained model and vectorizer
try:
    with open('model/stress_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model/vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    # If pickled model not found, train a new one
    # Load your dataset
    df = pd.read_csv('Stress.csv')
    
    # Prepare data
    X = df['text']
    y = df['label']
    
    # Initialize and fit vectorizer
    vectorizer = TfidfVectorizer()
    X_transformed = vectorizer.fit_transform(X)
    
    # Train model
    model = LogisticRegression()
    model.fit(X_transformed, y)
    
    # Save model and vectorizer
    import os
    os.makedirs('model', exist_ok=True)
    with open('model/stress_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('model/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

def get_stress_level(probability):
    """Convert probability to stress level category"""
    if probability < 0.3:
        return "Low"
    elif probability < 0.6:
        return "Moderate"
    elif probability < 0.8:
        return "High"
    else:
        return "Severe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input
        text = request.form['text']
        
        # Transform the input text
        text_transformed = vectorizer.transform([text])
        
        # Get prediction probability
        probability = model.predict_proba(text_transformed)[0][1]
        
        # Get stress level category
        stress_level = get_stress_level(probability)
        
        # Get recommendations based on stress level
        recommendations = recommender.generate_recommendations(probability)
        
        return render_template(
            'result.html',
            stress_level=stress_level,
            confidence=probability,
            recommendations=recommendations
        )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)