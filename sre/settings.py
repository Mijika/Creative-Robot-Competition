import os

#base properties
TITLE = "We AI Robot"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
FPS = 30
POWER = 1
MAIN_SECRION_TOGGLE = 1
SECTION_CHECK = [1, 1]# 오프닝 체크, 메인 체크

#path
PATH = os.getcwd()
#PATH = os.path.dirname(os.getcwd()) Atom은 되고 VS는 안 됨;;;;
FONT_DIR = os.path.join(PATH + "\\source\\font")
IMAGE_DIR = os.path.join(PATH + "\\source\\image")
SOUND_DIR = os.path.join(PATH + "\\source\\sound")
TEXT_DIR = os.path.join(PATH + "\\source\\text")
VIDEO_DIR = os.path.join(PATH + "\\source\\video")

#Font
HMKMRHD = 'HMKMRHD.TTF'

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255 ,255 ,0)
BROWN = (111, 109, 81)
OPENING_SECTION_BACKGROUND = (41, 64, 82)
OPENINH_SECTION_FONT_COLOR = (248, 228, 204)
MAIN_SECTION_BACKGROUND = (68, 114, 148)
MAIN_SECTION_MENUBAR = (41, 64, 82)
MAIN_SECTION_FONT_COLOR = (244, 214, 188)
#Image
SETTING_ICON = "메인화면_설정아이콘.png"
COOK_ICON = "메인화면_요리아이콘.png"
CCTV_ICON = "메인화면_CCTV아이콘.png"
CAMERA_ICON = "메인화면_카메라아이콘.png"
MARC_ICON = "메인화면_마크.png"
BACK_ICON = "세부화면_뒤로가기.png"