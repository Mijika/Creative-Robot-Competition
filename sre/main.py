import sys
import os
import time
import random

import pygame as pg
from settings import *
from sprites import *
from ui import  *

#from moviepy.editor import VideoFileClip

class Robot:
    #로봇 초기화
    def __init__(self):
        pg.init()
        pg.mixer.init()
        #기본 디스플레이 설정
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #상세 창 없는 디스플레시 설정
        #self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.NOFRAME)
        #라즈베리파이용 디스플레이 설정
        #self.screen = pg.display.set_mode((480, 320), pg.FULLSCREEN | pg.HWSURFACE | pg.DOUBLEBUF)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.opening = True #오프닝 스크린 실행 Boolean 값
        self.runing = True #프로그램 실행 Boolean 값
        self.load_date()

#-------------------메인 -------------------
    def main_new(self):
        self.setting_section = Setting_section(robot)
        self.cook_section = Cook_section(robot)
        self.camera_section = Camera_section(robot)
        self.cctv_section = Cctv_section(robot)

        self.main_menu = pg.sprite.Group()
        self.main_menu_setting = Menu(
            self.setting_icon, (SCREEN_WIDTH / 3), (SCREEN_HEIGHT / 3))
        self.main_menu_cook = Menu(
            self.cook_icon, (SCREEN_WIDTH / 3), (2 * (SCREEN_HEIGHT / 3)))
        self.main_menu_camera = Menu(
            self.camera_icon, (2 * (SCREEN_WIDTH / 3)), (SCREEN_HEIGHT / 3))
        self.main_menu_cctv = Menu(
            self.cctv_icon, (2 * (SCREEN_WIDTH / 3)), (2 * (SCREEN_HEIGHT / 3)))
        self.main_menu_marc = Menu(self.marc_icon, 60, 65)

        self.main_menu.add(self.main_menu_marc)
        self.main_menu.add(self.main_menu_setting)
        self.main_menu.add(self.main_menu_cook)
        self.main_menu.add(self.main_menu_camera)
        self.main_menu.add(self.main_menu_cctv)

        self.main_loop = True
        self.main_run()

    def main_run(self):
        print("메인 섹션 실행")
        while self.main_loop:  #메인 루프
            self.clock.tick(FPS)
            self.main_events()
            self.main_update()
            self.main_draw()
        pg.mixer.music.fadeout(500) #배경음이 갑자기 꺼지지 않고 점점 꺼지게 함


    def main_events(self):
        #main loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.main_loop:
                    self.main_loop = False
                    self.runing = False
                    self.opening = False
                print("프로그램 종료")
            elif event.type == pg.MOUSEBUTTONDOWN:
                # 1 is the left mouse button, 2 is middle, 3 is right.
                if event.button == 1:
                    if self.main_menu_setting.mouse_ckeck(event.pos):
                        print("셋팅 섹션")
                        self.setting_section.new()
                    elif self.main_menu_cook.mouse_ckeck(event.pos):
                        print("요리 섹션")
                        self.cook_section.new()
                    elif self.main_menu_camera.mouse_ckeck(event.pos):
                        print("카메라 섹션")
                        self.camera_section.new()
                    elif self.main_menu_cctv.mouse_ckeck(event.pos):
                        print("CCTV 섹션")
                        self.cctv_section.new()

    def main_update(self):
        self.time = time.strftime("%Y %m %d %I:%M").split(" ")
        self.time = self.time[0] + "년 " + self.time[1] + "월 " + self.time[2] + "일 " + self.time[3]
        self.main_menu.update()

    def main_draw(self):
        pg.draw.rect(
            self.screen, MAIN_SECTION_BACKGROUND, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        pg.draw.rect(
            self.screen, MAIN_SECTION_MENUBAR, [0, 0, SCREEN_WIDTH, 60])

        self.main_menu.draw(self.screen)

        self.draw_text("메인 페이지 입니다.", 20,
                       MAIN_SECTION_FONT_COLOR, (SCREEN_WIDTH / 2), 30)
        self.draw_text(
            self.time, 15, MAIN_SECTION_FONT_COLOR, 7 * (SCREEN_WIDTH / 9) + 60, 30)

        pg.display.update()

#--------------------메인 ----------------------




#--------------------오프닝 ---------------------
    #오프닝 스크린
    def show_opening_screen(self):
        print("오프닝 시작")
        pg.mixer.music.load(os.path.join(SOUND_DIR, 'Background_sound1.mp3'))
        pg.mixer.music.play(loops=-1)
        self.opening_new()

    def opening_new(self):
        self.opening_sprites_group = pg.sprite.Group()
        self.opening_tick = pg.time.get_ticks()
        self.opening_sprites = Opening(self)
        self.opening_sprites_group.add(self.opening_sprites)
        self.opening_run()

    def opening_run(self):
        #opening loop
        self.opening_playing = True
        while self.opening_playing:
            self.clock.tick(FPS)
            self.opening_events()
            self.opening_update()
            self.opening_draw()

    def opening_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.opening_playing:
                    self.opening_playing = False
                    self.runing = False
                print("프로그램 종료")

    def opening_update(self):
        self.opening_sprites_group.update()

    def opening_draw(self):
        pg.draw.rect(self.screen, OPENING_SECTION_BACKGROUND, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])

        #오프닝 멘트 처리 로직
        if self.opening_sprites.step == 0:
            pg.draw.rect(self.screen, OPENING_SECTION_BACKGROUND, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        elif self.opening_sprites.step == 1:
            self.draw_text("안녕하세요.", 70, OPENINH_SECTION_FONT_COLOR, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        elif self.opening_sprites.step == 2:
            self.draw_text("로봇을 부팅중입니다.", 70, OPENINH_SECTION_FONT_COLOR, (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
        elif self.opening_sprites.step == 3:
            pg.draw.rect(self.screen, OPENING_SECTION_BACKGROUND, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        else:
            print("오프닝 종료")
            self.opening_playing = False
            self.opening = False

        pg.display.update()
#-------------------------------------------------------

    #필요한 외부 데이터를 불러오는 함수
    def load_date(self):
        #image
        self.setting_icon = pg.image.load("../source/image/" + SETTING_ICON).convert_alpha()
        self.cook_icon = pg.image.load("../source/image/" + COOK_ICON).convert_alpha()
        self.camera_icon = pg.image.load("../source/image/" + CCTV_ICON).convert_alpha()
        self.cctv_icon = pg.image.load("../source/image/" + CAMERA_ICON).convert_alpha()
        self.marc_icon = pg.image.load("../source/image/" + MARC_ICON).convert_alpha()
        self.back_icon = pg.image.load("../source/image/" + BACK_ICON).convert_alpha()

        #txt
        self.font_hmkmrhd = "../source/font/" + HMKMRHD

        #sound(효과음)
        #self.Background_sound = pg.mixer.Sound(os.path.join(SOUND_DIR, 'Background_sound1.mp3'))

    #화면에 텍스트 처리를 위한 메서드
    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_hmkmrhd, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
        #render(text, antialias, color, background=None) -> Surface

if __name__ == "__main__":
    robot = Robot()
    """
    while robot.opening:
        robot.show_opening_screen()
        while robot.runing:
            robot.main_new()
    """
    robot.main_new()

pg.quit()
