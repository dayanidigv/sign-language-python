# Hand Gesture Recognition with Telegram Notification
This project leverages **OpenCV** and **MediaPipe** to detect hand gestures via a webcam and subsequently sends notifications to a Telegram bot based on the identified gestures. The system recognizes several hand gestures and transmits both a photo of the detected gesture and a corresponding message to a predefined Telegram chat.

## Requirements

- Python 3.7 or higher
- OpenCV (`cv2`)
- Mediapipe
- Requests (`requests`)
- Python `dotenv` for reading environment variables

## Installation

### 1. Clone the repository:


```
git clone https://github.com/dayanidigv/sign-language-python/
```


### 2. Install dependencies:
   
```
pip install opencv-python mediapipe requests python-dotenv
```

### 3. Setup

#### Telegram Bot Setup:

1. **Create a Telegram bot** by chatting with [@BotFather](https://t.me/botfather) on Telegram.
2. **Obtain your bot's API token** from @BotFather after creating the bot.
3. **Create a Telegram group or chat** where you want the bot to send notifications.
4. **Note down the chat ID** of the group or chat. You can find this by adding the bot to the group and using the Telegram API to get the chat ID, or by chatting with the bot and capturing the chat ID through the API.

#### Environment Variables:

1. **Create a `.env` file** in the root directory of your project.
2. Add the following lines to the `.env` file, replacing the placeholders with your actual bot token and chat ID:

```
BOT_TOKEN=<Your_Bot_Token>
CHAT_ID=<Your_Chat_ID>
```
### 4. Running the Project
 - Ensure your webcam is connected and recognized by your system.
- Run the Python script:
  
```
Python tele_sign_language.py
```

### 5. Recognized Gestures
The system currently recognizes the following gestures:

- I need Help: Index and middle fingers raised with thumb down.
- I Love You: Thumb, index, and pinky fingers raised.
- I am so hungry: Thumb, index, and middle fingers raised.
- I am alright: Thumb and pinky fingers raised.
- Super: Index, middle, and pinky fingers raised.
- Please Smile: Index finger raised.
- Not okay: Thumb and index fingers raised.
- Thank you: All fingers raised.
- I am okay: Index, middle, and ring fingers raised.
- I am sad: Only thumb raised.
  
### 6. Code Structure
```
sign-language-python/
├── tele_sign_language.py  # Main Python script
├── .env                        # Environment file
├── README.md                   # This file
└── captured_photo.jpg          # Captured image (generated during run)
```
### Note:

- Adjust the gesture recognition logic in hand_gesture_recognition.py to recognize additional gestures as needed.
- For more advanced usage, consider exploring techniques like machine learning or deep learning to improve gesture recognition accuracy.
- Remember to replace <Your_Bot_Token> and <Your_Chat_ID> with your actual Telegram bot token and chat ID.
  
Feel free to customize this README to provide more specific instructions and details tailored to your project.


### Key Updates:

- The structure is simplified with clearer headings and instructions.
- Added the **Telegram Bot Setup** and **.env** file creation instructions.
- Clarified the usage of environment variables and code setup.
