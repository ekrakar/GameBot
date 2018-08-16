#routines for the accounts to run when doing particular activities
import pyautogui
import time
from runescape import talk

pyautogui.PAUSE = .05
pyautogui.FAILSAFE = True


def skill(type='clay', cur=0):
    if type == 'clay':
        if cur % 2 == 0 and cur <= 27:# south rock
            pyautogui.moveTo(961, 584, duration=.05)
            pyautogui.click()
            return 3, cur + 1
        if cur % 2 == 1 and cur <= 27:# north rock
            pyautogui.moveTo(962, 485, duration=.05)
            pyautogui.click()
            return 3, cur + 1
        if cur == 28:# open teleports
            pyautogui.moveTo(1737, 205, duration=.05)
            pyautogui.click()
            return 1, cur + 2
        if cur == 30:#teleport
            pyautogui.moveTo(951, 445, duration=.05)
            pyautogui.click()
            return 5, cur + 1
        if cur == 31:#teleport
            talk.bye()
            return 16, cur + 1
        if cur == 32:#head towards bank
            pyautogui.moveTo(600, 786, duration=.05)
            pyautogui.click()
            return 4, cur + 1
        if cur == 33:#open bank
            pyautogui.moveTo(627, 733, duration=.05)
            pyautogui.click()
            return 3, cur + 1
        if cur == 34:#bank and start back
            pyautogui.moveTo(987, 803, duration=.05)
            pyautogui.click()
            pyautogui.moveTo(1832, 223, duration=.05)
            pyautogui.click()
            return 11, cur + 1
        if cur == 35:#back to cave
            pyautogui.moveTo(1744, 185, duration=.05)
            pyautogui.click()
            return 10, cur + 1
        if cur == 36:#endter cave
            pyautogui.moveTo(800, 700, duration=.05)
            pyautogui.click()
            return 10, cur + 1
        if cur == 37:#fix camera move towards rocks
            pyautogui.moveTo(1741, 71, duration=.05)
            pyautogui.click()
            pyautogui.keyDown('up')
            time.sleep(1)
            pyautogui.keyUp('up')
            pyautogui.moveTo(150, 115, duration=.05)
            pyautogui.click()
            return 15, 0


def skillobj(type='cow', cur=0, output=[]):
    if type == 'cow':
        if cur == 0:# get init picture
            return 0, cur + 1, False, 1
        if (cur >= 1 and cur <= 7) or (cur >= 12 and cur <= 18) or (cur >= 23 and cur <= 30):# kill cow
            if output == []:
                return 0, cur, False, 1
            else:
                print(output[0][2])
                pyautogui.moveTo(288 + 1344 * output[0][2], 162 + 756 * output[0][1], duration=.1)
                pyautogui.click()
                if cur == 7:
                    return 4, cur + 1, False, 3
                else:
                    return 4, cur + 1, False, 1
        if cur == 8 or cur == 10 or cur == 19 or cur == 21 or cur == 31 or cur == 33:# click hide
            if output != []:
                pyautogui.moveTo(288 + 1344 * output[0][2], 162 + 756 * output[0][1], duration=.1)
                pyautogui.click()
            return 4, cur + 1, True, -1
        if cur == 9 or cur == 11 or cur == 20 or cur == 22 or cur == 32 or cur == 34:# loot hide
            pic = 2
            picbool = False
            if cur == 11:
                pic = 1
            if cur == 34:
                pic = -1
                picbool = True
            print(list(pyautogui.locateAllOnScreen('screanshots/cowhide.png')))
            if list(pyautogui.locateAllOnScreen('screanshots/cowhide.png')) != []:
                num = len(list(pyautogui.locateAllOnScreen('screanshots/cowhide.png'))) - 1
                pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('screanshots/cowhide.png')))
                for i in range(0, num):
                    pyautogui.click()
            return 0, cur + 1, picbool, pic
        if cur == 35:# open teleports
            pyautogui.moveTo(1737, 205, duration=.05)
            pyautogui.click()
            return 1, cur + 1, True, -1
        if cur == 36:#teleport
            pyautogui.moveTo(951, 445, duration=.05)
            pyautogui.click()
            return 21, cur + 1, True, -1
        if cur == 37:#head towards bank
            pyautogui.moveTo(600, 786, duration=.05)
            pyautogui.click()
            return 4, cur + 1, True, -1
        if cur == 38:#open bank
            pyautogui.moveTo(627, 733, duration=.05)
            pyautogui.click()
            return 3, cur + 1, True, -1
        if cur == 39:#bank
            pyautogui.moveTo(987, 803, duration=.05)
            pyautogui.click()
            return .1, cur + 1, True, -1
        if cur == 40:# open teleports
            pyautogui.moveTo(1737, 205, duration=.05)
            pyautogui.click()
            return 1, cur + 1, True, -1
        if cur == 41:#teleport
            pyautogui.moveTo(1022, 565, duration=.05)
            pyautogui.click()
            return 5, cur + 1, True, -1
        if cur == 42:#bye
            talk.bye()
            return 16, cur + 1, True, -1
        if cur == 43:#move
            pyautogui.moveTo(1908, 118, duration=.05)
            pyautogui.click()
            return 10, cur + 1, True, -1
        if cur == 44:#move
            pyautogui.moveTo(1820, 64, duration=.05)
            pyautogui.click()
            return 9, cur + 1, True, -1
        if cur == 45:#move
            pyautogui.moveTo(1791, 66, duration=.05)
            pyautogui.click()
            return 9, cur + 1, True, -1
        if cur == 46:#gate
            pyautogui.moveTo(1033, 500, duration=.05)
            pyautogui.click()
            return 2, cur + 1, True, -1
        if cur == 47:#move
            pyautogui.moveTo(1845, 179, duration=.05)
            pyautogui.click()
            return 6, 1, False, 1

