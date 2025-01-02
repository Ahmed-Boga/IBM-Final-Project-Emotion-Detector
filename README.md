# NLP Emotion Detector

## Overview
The **NLP Emotion Detector** is a web-based application that uses Natural Language Processing (NLP) to detect emotions in text. It provides scores for the emotions of anger, disgust, fear, joy, and sadness and identifies the dominant emotion in the analyzed text.

This project is the final submission for an IBM certification program, showcasing skills in Python, Flask, HTML, JavaScript, and API integration.

---

## Features
- Detects emotions (anger, disgust, fear, joy, sadness) from user-provided text.
- Highlights the dominant emotion based on the analyzed text.
- Offers a user-friendly web interface for emotion detection.
- Includes automated unit tests for core functionality.

---

## Project Structure
IBM-Final-Project-Emotion-Detector/
│
├── Emotion_detector/
│   ├── [EmotionDetection.py](http://emotiondetection.py/)         # Core logic for emotion detection using IBM Watson API
│
├── templates/
│   ├── index.html                  # Main frontend page for user interaction
│
├── static/
│   ├── mywebscript.js              # JavaScript logic for handling frontend interaction
│
├── [server.py](http://server.py/)                       # Flask web server for handling requests
├── test_emotion_detection.py       # Unit tests for the emotion detection logic
└── [README.md](http://readme.md/)                       # Project documentation


## Installation and Setup
**Clone the Repository**
   ```
   git clone https://github.com/your-username/IBM-Final-Project-Emotion-Detector.git
   cd IBM-Final-Project-Emotion-Detector
   ```
1. **Install Dependencies**
Ensure Python 3.7+ is installed. Then, install the required Python libraries:
    
    ```
    pip install flask requests
    
    ```
    
2. **Run the Application**
    
    ```
    python server.py
    
    ```
    
3. **Access the Application**
Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

1. Open the application in your browser.
2. Enter the text to analyze in the provided input field.
3. Click **Run Sentiment Analysis** to detect the emotions.
4. The system will display scores for each emotion and identify the dominant one.

---

## API Integration

The emotion detection functionality leverages the Watson NLP API for analyzing text. Make sure you have internet access when running the application to interact with the API.

---

## Testing

To run unit tests and validate the functionality:

```
python -m unittest test_emotion_detection.py

```

---

## Technologies Used

- **Python**: Core language for backend logic and server implementation.
- **Flask**: Framework for building the web server and API endpoints.
- **HTML/CSS**: Frontend interface for user interactions.
- **JavaScript**: Handles client-side operations and API requests.
- **Bootstrap**: Ensures a responsive and modern UI.

---

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of changes.

---

## License

This project is licensed under the MIT License.

---

## Author

- **Ahmed**
- IBM Final Project - Emotion Detector

For any queries, please contact.

