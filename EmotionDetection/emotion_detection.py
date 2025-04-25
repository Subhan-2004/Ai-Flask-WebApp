import requests
import json

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    try:
        if isinstance(response.text, str):
            formatted_response = json.loads(response.text)
        else:
            formatted_response = response.text

        emotion_data = formatted_response['emotionPredictions'][0]['emotion']

        # Extracting individual scores
        anger_score = emotion_data['anger']
        disgust_score = emotion_data['disgust']
        fear_score = emotion_data['fear']
        joy_score = emotion_data['joy']
        sadness_score = emotion_data['sadness']

        # Getting the dominant emotion
        dominant_emotion = max(emotion_data, key=emotion_data.get)

        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    
    except Exception as e:
        print("Error parsing response:", e)
        print("Raw response:", response.text)
        return None
