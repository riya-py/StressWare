# Stressware: Mental Health Analysis System

A web-based application that analyzes text input to detect stress levels and provides personalized recommendations for stress management.

## Features 

- Text-based stress level Analysis using machine learning
- Real-time analysis and predictions
- Personalized recommendations based on stress levels
- Responsive web interface
- Multiple stress management categories:
  - Immediate actions
  - Breathing exercises
  - Physical activities
  - Mindfulness practices
  - Lifestyle changes
  - Social support 

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **NLP**: NLTK, TfidfVectorizer

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Stressware.git
cd Stressware
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
stressware: mental health analysis system
├── app.py                  # Main Flask application
├── recommendations.py      # Recommendation system
├── requirements.txt        # Project dependencies
├── Stressware.ipynp        # Training the Model
├── static/
│   └── style.css          # CSS styles
├── templates/
│   ├── index.html         # Home page
│   ├── result.html        # Results page
│   ├── 404.html          # Error page
│   └── 500.html          # Server error page
├── model/                 # Saved ML models
│   ├── stress_model.pkl
│   └── vectorizer.pkl
└── README.md             # Project documentation
```

## Usage

1. Access the web interface through your browser
2. Enter your thoughts and feelings in the text area
3. Click "Analyze" to get your stress assessment
4. Review your stress level and personalized recommendations
5. Follow the suggested recommendations for stress management

## Model Training

The system uses multiple machine learning models for stress detection:
- Logistic Regression
- Multinomial Naive Bayes
- Decision Trees
- Random Forest
- AdaBoost
- K-Nearest Neighbors

The best performing model is automatically selected and saved for predictions.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Stressware: Mental Health Analysis System
A comprehensive mental health analysis system that detects stress levels and provides personalized wellness recommendations.

## Safety Note:
This project includes helpline numbers specific to India and the US. Adaptations for other regions can be made as needed.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset sources and contributors
- Open-source libraries and frameworks
- Mental health resources and guidelines

## Contact

riya - [@riya_pyy](https://twitter.com/riya_pyy) - riya.rk006@gmail.com

Project Link: [https://github.com/riya-py/Stressware](https://github.com/riya-py/Stressware)
