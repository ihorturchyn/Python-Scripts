#!/usr/bin/env
import pyautogui
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.click(100,100, button='left')
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.click(200,100, button='left')
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.click(200,200, button='left')
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.click(200,200, button='left')
