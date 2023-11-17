from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

target_color1 = (229, 229, 229) # WHITE RGB 
target_color2 = (0, 0, 0) # BLACK RGB
#target_color3 = (105, 150, 0)

# WAIT 5 TO TAB TO GAME
time.sleep(5)

# SET FISHING ROD TO HOTKEY = 5
keyboard.press("5")
time.sleep(0.01)
keyboard.release("5")

# Wait for 7 seconds for animations to finishe
time.sleep(7)

while True:
  if pyautogui.locateOnScreen('fishing.jpg', grayscale=True, confidence=0.6) is not None:
    keyboard.press("g")
    time.sleep(0.01)
    keyboard.release("g")
    while not pyautogui.pixelMatchesColor(959, 346, target_color2, tolerance=20):
        time.sleep(0.01)  # wait for a short time before checking again
    keyboard.press("e")
    time.sleep(0.01)
    keyboard.release("e")
  # B TO QUIT THE SCRIPT HAVE TO BE OUTSIDE OF GAME, ELSE U CAN CTRL + C IN THE TERMINAL TO TERMINATE THE SCRIPT
  if keyboard.is_pressed('b'):
    break
  time.sleep(2)