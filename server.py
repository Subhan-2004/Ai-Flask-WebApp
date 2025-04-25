from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def get_emotion():
    # Get the text input from query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Please provide text to analyze using ?textToAnalyze=your_text_here"

    try:
        # Analyze emotion using your function
        result = emotion_detector(text_to_analyze)

        # Format the result as required
        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, "
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

        return response

    except Exception as e:
        return f"Error processing the request: {str(e)}"

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
