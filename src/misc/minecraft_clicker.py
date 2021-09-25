# -*- coding: utf-8 -*-
import time

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


def copy_and_paste():
    keyboard.wait('shift')
    original_coord_1 = 31
    destination_coord = 112
    while True:
        pyautogui.write('/clone 117 {} 25 236 {} 155 -3506 {} 13697 replace'.format(original_coord_1, original_coord_1+1, destination_coord))
        pyautogui.press('enter')
        original_coord_1 += 1
        destination_coord += 1
        if keyboard.is_pressed('esc'):
            keyboard.wait('shift')


if __name__ == '__main__':
    copy_and_paste()
