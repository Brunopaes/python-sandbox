# -*- coding: utf-8 -*-
import pyautogui
import keyboard
import time


def right_clicker():
    keyboard.wait('shift')
    while True:
        pyautogui.rightClick()
        if keyboard.is_pressed('esc'):
            keyboard.wait('shift')


def left_clicker():
    keyboard.wait('shift')
    while True:
        pyautogui.leftClick()
        if keyboard.is_pressed('esc'):
            keyboard.wait('shift')
        time.sleep(4)


if __name__ == '__main__':
    right_clicker()
