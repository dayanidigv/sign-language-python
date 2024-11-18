import cv2
import mediapipe as mp
import time
import os
import requests as r
import threading

def sendPhoto(chat_id, file):
    try:
        path = {"photo": open(file, "rb")}
        print("Image read successfully..") 
        resp = r.post(f"https://api.telegram.org/{os.getenv('BOT_TOKEN')}/sendPhoto?chat_id={chat_id}&caption=", files=path)
        if resp.status_code == 200:
            print("Successfully sent...")
        else:
            print("Failed to send")
    except Exception as e:
        print(f"Error sending photo: {e}")

def sendMsg(chat_id, txt):
    try:
        resp = r.post(f"https://api.telegram.org/{os.getenv('BOT_TOKEN')}/sendMessage?chat_id={chat_id}&text={txt}")
        if resp.status_code == 200:
            print("Successfully sent...")
        else:
            print("Failed to send")
    except Exception as e:
        print(f"Error sending message: {e}")

def text(txt):
    cv2.putText(image, txt, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
tipIds = [4, 8, 12, 16, 20]
cap = cv2.VideoCapture(0)
value = ""
key = ""
with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        ret, image = cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                myHands = results.multi_hand_landmarks[0]
                for id, lm in enumerate(myHands.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers = []
        if len(lmList) != 0:
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
            if k == ord('s'):
                print(len(lmList))
                print(fingers)
                print(lmList[0], lmList[20])
                print(lmList[0][1], lmList[20][1])
                
            if len(lmList) == 21:
                if fingers == [1, 0, 1, 0, 0]:
                    if lmList[0][1] < lmList[20][1]:
                        text("*****")
                        value = "*****"
                        
                if fingers == [0, 1, 1, 0, 1]:
                    if lmList[0][1] > lmList[20][1]:
                        text("I need Help")
                        value = "I need Help"

                if fingers == [1, 1, 0, 0, 1]:
                    if lmList[0][1] < lmList[20][1]:
                        text("I Love You")
                        value = "I Love You"

                if fingers == [1, 1, 1, 0, 0]:
                    if lmList[0][1] < lmList[20][1]:
                        text("I am so hungry")
                        value = "I am so hungry"

                if fingers == [0, 0, 0, 0, 1]:
                    if lmList[0][1] < lmList[20][1]:
                        text("I am alright")
                        value = "I am alright"

                if fingers == [0, 0, 1, 1, 1]:
                    if lmList[0][1] > lmList[20][1]:
                        text("Super")
                        value = "Super"

                if fingers == [0, 1, 0, 0, 0]:
                    if lmList[0][1] < lmList[20][1]:
                        text("Please Smile")
                        value = "Please Smile"

                if fingers == [1, 1, 0, 0, 0]:
                    if lmList[0][1] < lmList[20][1]:
                        text("Not okay")
                        
            if len(lmList) == 42:
                if fingers == [1, 1, 1, 1, 1]:
                    if lmList[0][1] < lmList[20][1]:
                        text("Thank You")
                        value = "Thank You"

                if fingers == [0, 1, 1, 1, 1]:
                    if lmList[0][1] < lmList[20][1]:
                        text("I am okay")

                if fingers == [1, 0, 0, 0, 0]:
                    if lmList[0][1] > lmList[20][1]:
                        text("I am sad")

        cv2.imshow("Frame", image)
        if key != value:
            photo_filename = "captured_photo.jpg"
            cv2.imwrite(photo_filename, image)
            # Send the photo in a separate thread
            my_photo_thread = threading.Thread(target=sendPhoto, args=(os.getenv('CHAT_ID'), photo_filename))
            my_photo_thread.start()
            my_thread = threading.Thread(target=sendMsg, args=(os.getenv('CHAT_ID'), value)) 
            # Start the thread
            my_thread.start()
            key = value 
            
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
