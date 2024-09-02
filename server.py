"""
This module contains the Flask web server for the Emotion Detector application.

It defines routes for emotion detection and rendering the main index page.
The application uses a pre-trained model to detect emotions from the input text and returns
the dominant emotion along with the scores for anger, disgust, fear, joy, and sadness.

Routes:
- /emotionDetector: Accepts GET requests with text input and returns emotion analysis.
- /: Renders the main index HTML page.
"""

from flask import Flask, render_template, request
from Emotion_detector.EmotionDetection import emotion_detector

# Initiate the Flask app
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Route for processing emotion detection on input text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    dominant_emotion = result.get('dominant_emotion')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger_score = result.get('anger')
    disgust_score = result.get('disgust')
    fear_score = result.get('fear')
    joy_score = result.get('joy')
    sadness_score = result.get('sadness')

    response_message = (
        f"For the given statement, the system response is 'anger': {anger_score}, "
        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
    )
    return response_message

@app.route("/")
def render_index_page():
    """
    Route for rendering the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
