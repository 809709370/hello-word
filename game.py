
import random
import sys
class sprite:
    """这是一个基类"""
    move_len = (-3,-2,2,3)

    def __init__(self,postion1 = None):
        self.energy = 0
        self.step = random.choice(sprite.move_len)
        if postion1 is None:
            self.postion = random.randint(0,20)
        else:
            self.postion = postion1
    def gojump(self):
        self.step = random.choice(sprite.move_len)
        if(self.postion + self.step >=0 and self.postion + self.step <=20):
            self.postion += self.step

class Ant(sprite):
    """这是一个蚂蚁类"""
    def __init__(self,postion = None):
        super().__init__(postion)
        self.energy = 6


class Worm(sprite):
    """这是一个虫子类"""
    def __init__(self,postion = None):
        super().__init__(postion)

class Map:
    """这是一个地图类"""
    def __init__(self,ant1,worm1):
        self.ant1 =  ant1
        self.worm1 = worm1

    def gamestart(self):
        while(self.ant1.energy > 0):
             while(self.ant1.postion != self.worm1.postion):
                self.ant1.gojump()
                print("the ant:",self.ant1.postion)
                self.worm1.gojump()
                print("the worm:",self.worm1.postion)
             print("energy :",self.ant1.energy)
             self.ant1.energy = self.ant1.energy - 1
             self.ant1.postion = random.randint(0,20)
             self.worm1.postion = random.randint(0,20)
        print("energy is ",self.ant1.energy)
        print("game over")

class father1:
    def __init__(self):
        print("father1")
class father2:
    def __init__(self):
        print("father2")
class son(father1,father2):
    def __init__(self):
        father2.__init__(self)

if __name__ == "__main__":
    # ant1 = Ant()
    # worm1 = Worm()
    # map1 = Map(ant1,worm1)
    # map1.gamestart()
    Son = son()







