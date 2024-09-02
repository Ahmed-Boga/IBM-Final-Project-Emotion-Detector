import requests
import json

def emotion_detector(text_to_analyse):
    # Check if the input text is blank
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    # Define the URL for the sentiment analysis API
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    payload = {"raw_document": {"text": text_to_analyse}}

    # Set the headers with the required model ID for the API
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        formatted_response = json.loads(response.text)
        
        # Extract emotion scores
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Find the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return the formatted result
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None