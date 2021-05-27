# -*- coding: utf-8 -*-
import pyautogui
import keyboard


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


def scroll_up_down(list_=(200, -200)):
    keyboard.wait('shift')
    while True:
        for i in list_:
            pyautogui.scroll(i)
            if keyboard.is_pressed('esc'):
                keyboard.wait('shift')


if __name__ == '__main__':
    left_clicker()
