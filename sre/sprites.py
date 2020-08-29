import pygame as pg
from settings import *

#opening 클래스
class Opening(pg.sprite.Sprite):
    def __init__(self, robot):
        pg.sprite.Sprite.__init__(self)
        self.robot = robot
        self.step = 0

    def update(self):
                #오프닝 멘트 처리 로직
        self.current_time = pg.time.get_ticks()
        self.current_time = self.current_time - self.robot.opening_tick
        if self.current_time < 2500:
            self.step = 0
        elif self.current_time >= 2500 and self.current_time < 6000:
            self.step = 1
        elif self.current_time >= 6000 and self.current_time < 9000:
            self.step = 2
        elif self.current_time >= 9000 and self.current_time < 12000:
            self.step = 3
        else:
            self.step = 4

#main screen 메뉴
class Menu(pg.sprite.Sprite):
    def __init__(self, image, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        pass

    def mouse_ckeck(self, mouse):
        self.mouse = mouse
        self.width = self.rect[0] + self.rect[2]
        self.height = self.rect[1] + self.rect[3]

        if self.mouse[0] >= self.rect[0] and self.mouse[1] >= self.rect[1]:
            if self.mouse[0] <= self.width and self.mouse[1] <= self.height:
                return True
        return False
