from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

time.sleep(10)

# Press "5" key for the fishing rod
keyboard.press("5")
time.sleep(0.1)
keyboard.release("5")

# Wait for 7 seconds
time.sleep(7)

# Create a while loop to continuously check for the check point
while not keyboard.is_pressed("b"):
    if pyautogui.locateOnScreen('fishing.jpg', grayscale=True, confidence=0.8) is not None:
        print("Found fishing.jpg")
        keyboard.press("g")
        time.sleep(0.1)
        keyboard.release("g")

    # Wait for 15 seconds
    time.sleep(15)

    # Press "e" key to reel in when the middle pixel of black crosses the green area
    while not keyboard.is_pressed("e"):
        try:
            if pyautogui.locateOnScreen('reelin.jpg', confidence=0.75) is not None:
                print("Found reelin.jpg")
                keyboard.press("e")
                time.sleep(0.1)
                keyboard.release("e")

    # Wait for interaction to finish seconds
    time.sleep(6)
