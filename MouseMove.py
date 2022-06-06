import pyautogui, time

loc1 = pyautogui.locateOnScreen('item04.png', confidence = 0.7)

center = pyautogui.center(loc1)
pyautogui.moveTo(center)