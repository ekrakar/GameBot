#routines to move the character from one area to another
import pyautogui
import time
from runescape import talk

pyautogui.PAUSE = .05
pyautogui.FAILSAFE = True

def move(type='burthrope_bank', cur=0):
    if type == 'burthrope_bank':
        if cur == 0:# open teleports
            pyautogui.moveTo(1737, 205, duration=.05)
            pyautogui.click()
            return 1, cur + 1, True
        if cur == 1:#teleport
            pyautogui.moveTo(951, 445, duration=.05)
            pyautogui.click()
            return 5, cur + 1, True
        if cur == 2:#bye
            talk.bye()
            return 16, cur + 1, True
        if cur == 3:#head towards bank
            pyautogui.moveTo(600, 786, duration=.05)
            pyautogui.click()
            return 4, cur + 1, True
        if cur == 4:#open bank
            pyautogui.moveTo(627, 733, duration=.05)
            pyautogui.click()
            return 3, cur + 1, True
        if cur == 5:#bank
            pyautogui.moveTo(987, 803, duration=.05)
            pyautogui.click()
            pyautogui.moveTo(1020, 808, duration=.05)
            pyautogui.click()
            return 0, 0, False
    if type == 'ge':
        if cur == 0:# open teleports
            pyautogui.moveTo(1737, 205, duration=.05)
            pyautogui.click()
            return 1, cur + 1, type
        if cur == 1:#teleport
            pyautogui.moveTo(951, 445, duration=.05)
            pyautogui.click()
            return 21, cur + 1, type
        if cur == 2:#head towards bank
            pyautogui.moveTo(600, 786, duration=.05)
            pyautogui.click()
            return 4, cur + 1, type
        if cur == 3:#open bank
            pyautogui.moveTo(627, 733, duration=.05)
            pyautogui.click()
            return 3, cur + 1, type
        if cur == 4:#bank
            pyautogui.moveTo(987, 803, duration=.05)
            pyautogui.click()
            pyautogui.moveTo(1020, 808, duration=.05)
            pyautogui.click()
            return 0, 0, 'burthrope_bank'
    if type == 'clay_mine':
        if cur == 0:  # bank and start back
            pyautogui.moveTo(1832, 223, duration=.05)
            pyautogui.click()
            return 11, cur + 1, True
        if cur == 1:  # back to cave
            pyautogui.moveTo(1744, 185, duration=.05)
            pyautogui.click()
            return 10, cur + 1, True
        if cur == 2:  # endter cave
            pyautogui.moveTo(800, 700, duration=.05)
            pyautogui.click()
            return 10, cur + 1, True
        if cur == 3:  # fix camera move towards rocks
            pyautogui.moveTo(1741, 71, duration=.05)
            pyautogui.click()
            pyautogui.keyDown('up')
            time.sleep(1)
            pyautogui.keyUp('up')
            pyautogui.moveTo(150, 115, duration=.05)
            pyautogui.click()
            return 15, 0, False
    if type == 'lumbridge_cows':
        if cur == 0:# open bank search
            pyautogui.moveTo(645, 805, duration=.05)
            pyautogui.click()
            return .1, cur + 1, True
        if cur == 1:# type staff of air
            pyautogui.typewrite('staff of air', .1)
            pyautogui.press('enter')
            pyautogui.moveTo(661, 341, duration=.05)
            pyautogui.rightClick()
            pyautogui.moveTo(637,483, duration=.05)
            pyautogui.click()
            pyautogui.moveTo(1737, 205, duration=.05)
            pyautogui.click()
            return 1, cur + 1, True
        if cur == 2:#teleport
            pyautogui.moveTo(1022, 565, duration=.05)
            pyautogui.click()
            return 5, cur + 1, True
        if cur == 3:#bye
            talk.bye()
            return 16, cur + 1, True
        if cur == 4:#move
            pyautogui.moveTo(1908, 118, duration=.05)
            pyautogui.click()
            return 10, cur + 1, True
        if cur == 5:#move
            pyautogui.moveTo(1820, 64, duration=.05)
            pyautogui.click()
            return 9, cur + 1, True
        if cur == 6:#move
            pyautogui.moveTo(1791, 66, duration=.05)
            pyautogui.click()
            return 9, cur + 1, True
        if cur == 7:#gate
            pyautogui.moveTo(1033, 500, duration=.05)
            pyautogui.click()
            return 2, cur + 1, True
        if cur == 8:#move
            pyautogui.moveTo(1845, 179, duration=.05)
            pyautogui.click()
            return 6, 0, False

