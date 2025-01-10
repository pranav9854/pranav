import cv2
import cvzone
import random
import time
from cvzone.HandTrackingModule import HandDetector
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(maxHands=2)
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, PLAYER]
initialTime = 0  # Initialize initialTime

while True:
    imgBG = cv2.imread("project/BG.png")
    if imgBG is None:
        print("Error: Background image not found!")
        break  # Exit the loop if the background image isn't loaded correctly
    
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    imgScaled = cv2.resize(img, (400, 420))

    # find hands
    hands, img = detector.findHands(imgScaled)
    if startGame:
        if stateResult is False:
            timer = time.time() - initialTime  # Use initialTime here
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            if timer > 3:
                stateResult = True
                timer = 0
                if hands:
                    playermove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    if fingers == [0, 0, 0, 0, 0]:  # rock
                        playermove = 1
                    elif fingers == [1, 1, 1, 1, 1]:  # paper
                        playermove = 2
                    elif fingers == [0, 1, 1, 0, 0]:  # scissors
                        playermove = 3

                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'project/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # player wins
                    if (playermove == 1 and randomNumber == 3) or \
                        (playermove == 2 and randomNumber == 1) or \
                             (playermove == 3 and randomNumber == 2):
                                  scores[1] += 1
                               
                    # AI wins
                    elif (playermove == 3 and randomNumber == 1) or \
                        (playermove == 1 and randomNumber == 2) or \
                             (playermove == 2 and randomNumber == 3):
                                 scores[0] += 1          
                    if scores[1] >= 5:
                        print("Congrats! You won...")                        
                    elif scores[0] >= 5:
                        print("AI won. Better luck next time!!")
                        
    imgBG[234:654, 795:1195] = imgScaled
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
        cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
        cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    cv2.imshow("BG", imgBG)
    key = cv2.waitKey(1)
    if key == ord(' '):  # Start the game when space is pressed
        startGame = True
        initialTime = time.time()  # Initialize the timer when the game starts
        stateResult = False
    elif key == 27:  # Exit when the 'Esc' key is pressed
        print("game exited by the user") 
        break
