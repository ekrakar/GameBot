#manages the accounts and tells them when do change activities log out do their next action and various other things based on times.
from runescape import bot_object
import time
from datetime import timedelta
import pyautogui


class RunBot:
    def __init__(self, pools, video_capture):
        pyautogui.PAUSE = .15
        pyautogui.FAILSAFE = True

        self.cam = video_capture
        self.pools = pools
        self.start_time = time.time()
        self.step_timer = self.start_time
        self.downtime = 100
        self.login_time = 1440000
        self.break_timer = 0
        self.login_timer = self.login_time
        self.total_accounts = 1
        self.account_increments = [1, 5, 3, 4, 5, 6, 7, 8]
        self.set = 0
        self.accounts = []
        self.logout_timer = 300
        self.change_location = 3600
        self.change_timer = self.change_location
        self.AltTabTracker = [0, 1, 2, 3]
        self.AltTabLocs = [[381, 429], [671, 429], [970, 429], [1249, 429]]

    #main loop
    def update(self):
        while True:
            while self.break_timer > 0:#used to have the accounts logged out for a period of time
                end_time = time.time()
                dif = end_time - self.step_timer
                if int(dif) > 0:
                    self.break_timer -= dif
                    self.step_timer = end_time
                    print("Break time remaining: " + str(timedelta(seconds=int(round(self.break_timer)))))
                    if self.break_timer <= 0:
                        self.login_timer = self.login_time
                        self.change_timer = self.change_location

            for i in range(0, self.total_accounts):#creats the accounts and starts the loggin process
                self.accounts.append(bot_object.Bot(str(self.account_increments[i + (self.set * self.total_accounts)]), 'login', 380 + i * 20, self.pools[i], self.cam))#mining_clay or login
            if self.set == 1:
                self.set = 0
            else:
                self.set = 1

            #rotates bettween the accounts while logged in running their next actions until time is up then it starts the logout sequence
            while self.login_timer > 0:
                end_time = time.time()
                dif = end_time - self.step_timer
                if int(dif) > 0:
                    self.login_timer -= dif
                    self.change_timer -= dif
                    if self.change_timer <= 0:
                        self.change_timer = self.change_location
                        for i in range(0, self.total_accounts):
                            self.accounts[i].change()
                    self.step_timer = end_time
                    print("login time remaining: " + str(timedelta(seconds=int(round(self.login_timer)))))
                if self.login_timer <= 0:
                    self.logout_timer = 180
                    for i in range(0, self.total_accounts):
                        self.accounts[i].stop()
                else:
                    self.actions()

            #gives the accounts time to finish finish their routines and log out
            while self.logout_timer > 0:
                end_time = time.time()
                dif = end_time - self.step_timer
                if int(dif) > 0:
                    self.logout_timer -= dif
                    self.step_timer = end_time
                    print("logout time remaining: " + str(timedelta(seconds=int(round(self.logout_timer)))))
                    if self.logout_timer <= 0:
                        self.break_timer = self.downtime
                        self.accounts = []
                if self.logout_timer > 0:
                    self.actions()

    #if the account is ready for a action it preforms the next action
    def actions(self):
        for i in range(0, self.total_accounts):
            if self.accounts[i].proceed():
                if self.AltTabTracker[0] == i:
                    self.alttab(0, i)
                elif self.AltTabTracker[1] == i:
                    self.alttab(1, i)
                elif self.AltTabTracker[2] == i:
                    self.alttab(2, i)
                elif self.AltTabTracker[3] == i:
                    self.alttab(3, i)

    #keeps track of where each account is on the alt tab menu in windows
    def adjust(self, num):
        templist = [num]
        for i in range(0, self.total_accounts):
            if self.AltTabTracker[i] != num:
                templist.append(self.AltTabTracker[i])
        return templist

    #preforms the alt tab to switch between which account is being looked at
    def alttab(self, pos, i):
        if self.total_accounts > 1:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.moveTo(self.AltTabLocs[pos][0], self.AltTabLocs[pos][1], duration=.15)  
            pyautogui.click()
            pyautogui.keyUp('alt')
        self.accounts[i].nextaction()
        self.AltTabTracker = self.adjust(i)
