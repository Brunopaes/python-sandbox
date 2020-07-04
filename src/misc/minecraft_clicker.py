# -*- coding: utf-8 -*-
import pyautogui
import keyboard


def clicker():
    keyboard.wait('shift')
    while True:
        pyautogui.rightClick()
        if keyboard.is_pressed('esc'):
            keyboard.wait('shift')


if __name__ == '__main__':
    clicker()
