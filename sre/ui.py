import pygame as pg
from settings import *
from sprites import *
from abc import *

#기본 윈도우 구조
class Screen_panel(metaclass=ABCMeta):
    @abstractmethod
    def new(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def events(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Sub_panel(Screen_panel):
    """
        메인 화면에서 버튼을 클릭하면 나오는 섹션의 플레임
    """
    def __init__(self, robot):
        self.robot = robot

    def new(self):
        self.back = Menu(self.robot.back_icon,
                         (SCREEN_WIDTH / 4), (3*(SCREEN_HEIGHT/4)))
    def run(self):
        pass
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.loop:
                    self.loop = False
                    self.robot.main_loop = False
                    self.robot.runing = False
                    self.robot.opening = False
                print("프로그램 종료")
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    if self.back.mouse_ckeck(event.pos):
                        print("뒤로")
                        self.loop = False
    def update(self):
        pass
    def draw(self):
        pg.draw.rect(
            self.robot.screen, MAIN_SECTION_BACKGROUND, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        self.robot.screen.blit(self.back.image, self.back.rect)

#셋팅 섹션


class Setting_section(Sub_panel):
    def __init__(self, robot):
        super().__init__(robot)

    def new(self):
        super().new()
        self.setting_menu = pg.sprite.Group()
        self.loop = True
        self.run()

    def run(self):
        print("setting 섹션 실행")
        while self.loop:
            self.robot.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        super().events()


    def update(self):
        self.setting_menu.update()

    def draw(self):
        super().draw()
        pg.display.update()


#요리 섹션
class Cook_section(Sub_panel):
    def __init__(self, robot):
        self.robot = robot

    def new(self):
        self.loop = True
        self.run()

    def run(self):
        print("cook 섹션 실행")
        while self.loop:
            self.robot.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        super().events()

    def update(self):
        pass

    def draw(self):
        pass

#카메라 섹션


class Camera_section(Sub_panel):
    def __init__(self, robot):
        self.robot = robot

    def new(self):
        self.loop = True
        self.run()

    def run(self):
        print("camera 섹션 실행")
        while self.loop:
            self.robot.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        super().events()

    def update(self):
        pass

    def draw(self):
        pass

#CCTV 섹션


class Cctv_section(Sub_panel):
    def __init__(self, robot):
        self.robot = robot

    def new(self):
        self.loop = True
        self.run()

    def run(self):
        print("cctv 섹션 실행")
        while self.loop:
            self.robot.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        super().events()

    def update(self):
        pass

    def draw(self):
        pass
