#!-*- coding: utf8 -*-
import pyautogui
import time

time_ = 0.6


def draw():
    width, height = pyautogui.size()
    pyautogui.moveTo(0.00989 * height, 0.5515625 * width, time_)
    pyautogui.click()

    time.sleep(1)

    pyautogui.typewrite('paint', interval=0.1)

    time.sleep(1)

    pyautogui.hotkey('enter')

    pyautogui.moveTo(0.21770 * width, 0.05833 * height, time_)
    pyautogui.click()

    pyautogui.moveTo(0.18229 * width, 0.73888 * height, time_)
    pyautogui.dragTo(x=0.29947 * width, y=0.89537 * height, button='left')

    pyautogui.moveTo(0.31875 * width, 0.89537 * height, time_)
    pyautogui.dragTo(x=0.43229 * width, y=0.73425 * height, button='left')

    pyautogui.moveTo(0.38072 * width, 0.80648 * height, time_)
    pyautogui.dragTo(x=0.36145 * width, y=0.81388 * height, button='left')

    pyautogui.moveTo(0.3375 * width, 0.70740 * height, time_)
    pyautogui.dragTo(x=0.22916 * width, y=0.19814 * height, button='left')

    pyautogui.moveTo(0.27864 * width, 0.26388 * height, time_)
    pyautogui.dragTo(x=0.29531 * width, y=0.33518 * height, button='left')

    pyautogui.moveTo(0.20833 * width, 0.05833 * height, time_)
    pyautogui.click()

    pyautogui.moveTo(0.26197 * width, 0.34351 * height, time_)

    pyautogui.dragTo(x=0.34114 * width, y=0.36111 * height, button='left')
    pyautogui.dragTo(x=0.29427 * width, y=0.38333 * height, button='left')
    pyautogui.click()

    pyautogui.moveTo(0.29895 * width, 0.26944 * height, time_)
    pyautogui.dragTo(x=0.29687 * width, y=0.31481 * height, button='left')
    pyautogui.dragTo(x=0.29218 * width, y=0.29629 * height, button='left')


if __name__ == '__main__':
    width_, height_ = pyautogui.size()
    if (pyautogui.position().x != int(0.29218 * width_)) or \
            (pyautogui.position().y != int(0.29629 * height_)):
        time.sleep(0.5)
        draw()
