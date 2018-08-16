#logs in the account
import pyautogui
from random import *
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


def login(increment='001', cur=0, offset=0):
    if cur == 0:
        first = ''
        last = ''
        email = first + '.' + last + increment
        fullemail = email + '@'
        simppassword = '' + increment
        pyautogui.moveTo(916, 419, duration=float('.' + str(randint(10,20))))#email
        pyautogui.click()
        pyautogui.typewrite(fullemail, float('.' + str(randint(10,10))))
        pyautogui.moveTo(943, 485, duration=float('.' + str(randint(10,20))))#password
        pyautogui.click()
        pyautogui.typewrite(simppassword, float('.' + str(randint(10,10))))
        pyautogui.press('enter')
        return 13, 2
    elif cur == 2:
        pyautogui.moveTo(784, 144, duration=float('.' + str(randint(10,20))))#world select
        pyautogui.click()
        return 1, 3
    elif cur == 3:
        pyautogui.moveTo(1194, 248, duration=float('.' + str(randint(10,20))))#sort
        pyautogui.click()
        return 1, 4
    elif cur == 4:
        pyautogui.moveTo(950, offset, duration=float('.' + str(randint(10,20))))#world
        pyautogui.click()
        return 1, 5
    elif cur == 5:
        pyautogui.moveTo(1194, 248, duration=float('.' + str(randint(10,20))))#sort
        pyautogui.click()
        return 1, 6
    elif cur == 6:
        pyautogui.moveTo(983, 990, duration=float('.' + str(randint(10,20))))#play
        pyautogui.click()
        return 12, 7
    elif cur == 7:
        pyautogui.moveTo(1741, 71, duration=float('.' + str(randint(10,20))))#change camera
        pyautogui.click()
        pyautogui.keyDown('up')
        time.sleep(1)
        pyautogui.keyUp('up')
        return 0, -1

def logout():
    pyautogui.moveTo(1907, 39, duration=float('.' + str(randint(10, 20))))  # skip
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1065, 623, duration=float('.' + str(randint(10, 20))))  # skip
    pyautogui.click()
    return True
