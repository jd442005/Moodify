from deepface import DeepFace

def detect_mood(image_path):
    try:
        result = DeepFace.analyze(img_path=image_path, actions=["emotion"])
        mood = result[0]["dominant_emotion"]
        return mood
    except Exception as e:
        print(f"Error in mood detection: {e}")
        return None
