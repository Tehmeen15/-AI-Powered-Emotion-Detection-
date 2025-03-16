import cv2
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0)

# Open log file
log_file = open("emotion_log.txt", "a")

# Emotion descriptions
emotion_descriptions = {
    "angry": "Feeling of displeasure, rage, or frustration.",
    "disgust": "A strong sense of dislike or aversion.",
    "fear": "A response to perceived danger or threat.",
    "happy": "A state of joy, pleasure, and contentment.",
    "sad": "A feeling of sorrow, grief, or unhappiness.",
    "surprise": "A reaction to something unexpected.",
    "neutral": "A calm, emotionless state."
}

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    try:
        # Detect emotions
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        
        # Extract emotion and confidence
        emotion = result[0]['dominant_emotion']
        description = emotion_descriptions.get(emotion, "No description available.")
        
        # Log detected emotion
        log_file.write(f"Detected Emotion: {emotion} - {description}\n")
        log_file.flush()
        
        # Display emotion on frame
        cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, description, (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    except Exception as e:
        print("Error:", e)
    
    cv2.imshow('Emotion Detection', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
log_file.close()
