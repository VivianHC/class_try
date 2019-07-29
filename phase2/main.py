
import random


class Hero():

    def __init__(self, s, n, p):
        ''' 初始化函数 '''

        if len(s) > 0 and len(n) > 0 and len(p) > 0:
            self.skin = s       # skin
            self.name = n       # name
            self.position = p   # position

            self.ab_viability = random.randint(1, 100)
            self.ab_damage = random.randint(1, 100)
            self.ab_effect = random.randint(1, 100)
            self.ab_difficulty = random.randint(1, 100)
        else:
            self.skin = '英雄的皮肤'
            self.name = '英雄的姓名'
            self.position = '英雄的定位'

            self.ab_viability = 0
            self.ab_damage = 0
            self.ab_effect = 0
            self.ab_difficulty = 0
        return
