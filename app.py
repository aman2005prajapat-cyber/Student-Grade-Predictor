from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Student Grade Predictor</h1><p>Enter study hours in the URL like /predict?hours=8</p>"

@app.route('/predict')
def predict():
    # Get hours from the URL (e.g., /predict?hours=5)
    hours = request.args.get('hours', default=0, type=float)
    # Simple logic: 10 points per hour, max 100
    prediction = min(hours * 10, 100)
    return f"With {hours} hours of study, your predicted score is: {prediction}%"

if __name__ == '__main__':
    app.run(debug=True)
