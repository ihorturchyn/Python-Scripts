#!/usr/bin/env python
import pyautogui
for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.click(100,0, button='right')
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.click(0,100, button='right')
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.click(-100,0, button='right')
    pyautogui.moveRel(0, -100, duration=0.25)
    pyautogui.click(0,-100, button='right')