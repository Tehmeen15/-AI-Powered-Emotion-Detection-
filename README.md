# Emotion Detection using OpenCV and DeepFace

## Description
This project detects human emotions using a webcam feed and displays them in real time. It utilizes **DeepFace** for emotion recognition and **OpenCV** for video processing.

## Features
- Detects emotions: **Happy, Sad, Angry, Surprise, Fear, Disgust, and Neutral**
- Displays confidence scores for all detected emotions
- Logs detected emotions to a file
- Uses real-time webcam feed

## Installation
### Prerequisites
Ensure you have Python installed (preferably Python 3.8 or later).

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install -r requirements.txt
```

## Usage

### Running the Emotion Detection
1. Open the terminal or command prompt in the project directory.
2. Run the following command:
   ```sh
   python emotion_detect.py
   ```
3. The webcam will open, and emotions will be detected in real-time.
4. The detected emotions, along with their confidence scores, will be displayed on the screen.
5. Press `q` to exit the program.
6. Detected emotions will also be logged into a file named `emotion_log.txt`.

## Troubleshooting

- If some emotions are not detected, try improving lighting and facial expressions.
- Ensure all dependencies are installed correctly.

## License

This project is open-source and free to use.

```