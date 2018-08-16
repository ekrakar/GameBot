#each instance of this represents a account logged in. This manages the characters of the accounts.
import time
from random import *
from runescape import login
from runescape import skilling
from runescape import relocate


class Bot(object):
    def __init__(self, number, startaction, select, pool, cam):
        self.cam = cam
        self.pool = pool
        self.location = ''
        self.currentkind = ''
        self.currentaction = startaction
        self.currentstep = 0
        if int(number) < 10:
            self.increment = '00' + number
        else:
            self.increment = '0' + number
        self.start_time = time.time()
        self.step_time = self.start_time
        self.wait = 0
        self.logout = False
        self.stopped = False
        self.relocating = False
        self.worldselect = select
        self.changeaction = False
        self.detectionrequired = False
        self.havepic = False
        self.pictype = -1
        self.requestpic = False
    #preforms the next step in a set of predefined routines
    def nextaction(self):
        if not self.stopped:
            if self.currentstep == -1:
                self.findnextaction()
            if self.relocating:
                self.wait, self.currentstep, self.relocating = relocate.move(self.location, self.currentstep)
            else:
                print('action')
                if self.currentaction == 'login':
                    self.wait, self.currentstep = login.login(self.increment, self.currentstep, self.worldselect)
                if self.currentaction == 'logout':
                    self.stopped = login.logout()
                if self.currentaction == 'skilling':
                    if self.detectionrequired:
                        print('enter')
                        if self.havepic or self.currentstep == 0:
                            if self.pictype != -1:
                                obj = self.pool[2].get()
                            else:
                                obj = []
                            self.wait, self.currentstep, self.havepic, self.pictype = skilling.skillobj(self.currentkind, self.currentstep, obj)
                            if self.pictype != -1:
                                print('set')
                                self.requestpic = True
                    else:
                        self.wait, self.currentstep = skilling.skill(self.currentkind, self.currentstep)
                if self.changeaction and self.currentstep == 0:
                    self.currentstep = -1
                    self.changeaction = False
                    
    #updates the wait timer used to see if the previous action has been completed
    def updatewait(self):
        end_time = time.time()
        self.wait -= end_time - self.step_time
        self.step_time = end_time
        if self.wait > 0:
            return False
        else:
            return True

    #used for changing from 1 action to another
    def findnextaction(self):
        self.currentstep = 0
        if self.logout:
            self.currentaction = 'logout'
            self.changeaction = False
            self.relocating = False
            self.detectionrequired = False
            self.havepic = False
            return
        if self.currentaction == 'login':
            self.currentaction = ''
        if self.location == 'burthrope_bank':
            choice = randint(1, 1)
            if choice == 0:
                self.currentaction = 'skilling'
                self.currentkind = 'clay'
                self.location = 'clay_mine'
                self.relocating = True
                self.detectionrequired = False
                self.havepic = False
            if choice == 1:
                self.currentaction = 'skilling'
                self.currentkind = 'cow'
                self.location = 'lumbridge_cows'
                self.relocating = True
                self.detectionrequired = True
                self.havepic = False
        else:
            self.location = 'burthrope_bank'
            self.relocating = True
            self.changeaction = True
            self.detectionrequired = False
            self.havepic = False

    #will finish current routine then log out
    def stop(self):
        self.logout = True

    #used to identify when the current routine needs to be changed
    def change(self):
        self.changeaction = True

    #gets and processes another picture when needed
    def getpic(self):
        time.sleep(.1)
        frame = self.cam.read()
        frame = frame[108:612, 192:1088, :]
        self.pool[1].put([frame, self.pictype])
        print('requested')

    #checks if the picture is done processing
    def picready(self):
        if self.detectionrequired:
            if self.pool[2].empty():
                return False
            else:
                self.havepic = True
                return True
        else:
            return True

    #gets the pic to be used once its done processing
    def proceed(self):
        temp_bool = self.updatewait()
        if self.requestpic and self.wait <= .5:
            self.requestpic = False
            self.getpic()
            return True
        else:
            return temp_bool and (self.picready() or self.pictype == -1)



