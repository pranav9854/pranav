import cv2
import cvzone
import random
import time
from cvzone.HandTrackingModule import HandDetector

# Initialize the video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set the width of the frame
cap.set(4, 480)  # Set the height of the frame

# Initialize hand detector
detector = HandDetector(maxHands=1)

# Initialize variables
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [AI, PLAYER]
initialTime = 0

# Function to detect hand gesture (rock, paper, scissors)
def detect_gesture(fingers):
    if fingers == [0, 0, 0, 0, 0]:  # Rock gesture (closed fist)
        return 1
    elif fingers == [1, 1, 1, 1, 1]:  # Paper gesture (open hand)
        return 2
    elif fingers == [0, 1, 1, 0, 0]:  # Scissors gesture (V shape)
        return 3
    return None  # Invalid gesture

# Game loop
while True:
    imgBG = cv2.imread("project/BG.png")  # Make sure this path is correct!
    
    if imgBG is None:
        print("Error: Background image not found. Make sure the path is correct.")
        break

    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam.")
        break
    
    imgScaled = cv2.resize(img, (400, 420))  # Resize to fit into the background
    
    # Find hands in the camera feed
    hands, img = detector.findHands(imgScaled)

    if startGame:
        if not stateResult:
            # Timer logic
            timer = time.time() - initialTime
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)
            
            if timer > 3:
                stateResult = True
                timer = 0
                
                if hands:
                    playermove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)
                    
                    # Detect the player's move based on hand gesture
                    playermove = detect_gesture(fingers)
                    
                    if playermove is None:
                        print("Invalid gesture detected.")
                        continue  # Skip the current loop and wait for valid gesture
                    
                    # AI move
                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'project/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    if imgAI is None:
                        print(f"Error: AI image for move {randomNumber} not found.")
                        break
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))
                    
                    # Determine winner
                    if (playermove == 1 and randomNumber == 3) or \
                       (playermove == 2 and randomNumber == 1) or \
                       (playermove == 3 and randomNumber == 2):
                        scores[1] += 1  # Player wins
                    elif (playermove == 3 and randomNumber == 1) or \
                         (playermove == 1 and randomNumber == 2) or \
                         (playermove == 2 and randomNumber == 3):
                        scores[0] += 1  # AI wins
                    
                    # Check if the game is over
                    if scores[1] >= 5:
                        print("Congrats! You won...")
                        startGame = False
                    elif scores[0] >= 5:
                        print("AI won. Better luck next time!")
                        startGame = False
                
    # Display the camera feed on the BG image
    imgBG[234:654, 795:1195] = imgScaled
    
    # Display scores
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))  # Show AI's move
        cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)  # AI score
        cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)  # Player score
    
    # Display the BG image with the game overlay
    cv2.imshow("BG", imgBG)
    
    # Wait for a key press to start the game
    key = cv2.waitKey(1)
    if key == ord(' '):
        startGame = True
        initialTime = time.time()
        stateResult = False
