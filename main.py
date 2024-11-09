import pyautogui
import random

def move_mouse():
    while True:
        x = random.randint(0, pyautogui.size().width)
        y = random.randint(0, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=0.1)

move_mouse()
