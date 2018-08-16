#called when one of the accounts needs to talk
import pyautogui
from random import *
import time

pyautogui.PAUSE = .1
pyautogui.FAILSAFE = True


def greeting():
    pyautogui.press('enter')
    pyautogui.typewrite('hi', float('.' + str(randint(10,10))))
    pyautogui.press('enter')


def bye():
    pyautogui.press('enter')
    pyautogui.typewrite('bye', float('.' + str(randint(10, 10))))
    pyautogui.press('enter')
