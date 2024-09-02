from flask import Flask, render_template, request
from Emotion_detector.EmotionDetection import emotion_detector

# Initiate the Flask app
app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)
    
    # Run the emotion detector on the text
    result = emotion_detector(text_to_analyze)
    
    # Extract individual emotions and the dominant emotion
    dominant_emotion = result['dominant_emotion']
    
    # Check if the dominant emotion is None, indicating an error or invalid input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Extract scores for each emotion
    anger_score = result['anger']
    disgust_score = result['disgust']
    fear_score = result['fear']
    joy_score = result['joy']
    sadness_score = result['sadness']
    
    # Format the response as per the customer's request
    response_message = (f"For the given statement, the system response is 'anger': {anger_score}, "
                        f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
                        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}.")
    
    return response_message

@app.route("/")
def render_index_page():
    """
    This function renders the main HTML page for the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Run the Flask application on localhost:5000
    app.run(host="0.0.0.0", port=5000)