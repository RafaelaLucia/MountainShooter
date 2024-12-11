# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (237, 28, 36)
C_BLACK = (0, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Level2Bg6': 6,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 1,
    'Level3Bg3': 2,
    'Level3Bg4': 3,
    'Level3Bg5': 4,
    'Level3Bg6': 5,
    'Level3Bg7': 6,
    'Level3Bg8': 7,
    'Level3Bg9': 8,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 2,
    'Enemy2Shot': 5,
    'Enemy3': 2,
    'Enemy3Shot': 5,
    'Enemy4': 2,
    'Enemy4Shot': 5,
    'Enemy5': 3,
    'Enemy5Shot': 5,
    'Enemy6': 3,
    'Enemy6Shot': 5,
    'Explosion': 0,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Level2Bg6': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Level3Bg4': 999,
    'Level3Bg5': 999,
    'Level3Bg6': 999,
    'Level3Bg7': 999,
    'Level3Bg8': 999,
    'Level3Bg9': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'Enemy3': 60,
    'Enemy3Shot': 1,
    'Enemy4': 60,
    'Enemy4Shot': 1,
    'Enemy5': 60,
    'Enemy5Shot': 1,
    'Enemy6': 60,
    'Enemy6Shot': 1,
    'Explosion': 0,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'Level3Bg6': 0,
    'Level3Bg7': 0,
    'Level3Bg8': 0,
    'Level3Bg9': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
    'Enemy3': 1,
    'Enemy3Shot': 15,
    'Enemy4': 1,
    'Enemy4Shot': 15,
    'Enemy5': 1,
    'Enemy5Shot': 25,
    'Enemy6': 1,
    'Enemy6Shot': 25,
    'Explosion': 0,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Level3Bg4': 0,
    'Level3Bg5': 0,
    'Level3Bg6': 0,
    'Level3Bg7': 0,
    'Level3Bg8': 0,
    'Level3Bg9': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 125,
    'Enemy3Shot': 0,
    'Enemy4': 125,
    'Enemy4Shot': 0,
    'Enemy5': 125,
    'Enemy5Shot': 0,
    'Enemy6': 125,
    'Enemy6Shot': 0,
    'Explosion': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
    'Enemy3': 100,
    'Enemy4': 100,
    'Enemy5': 100,
    'Enemy6': 100,
    'Explosion': 0,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_RSHIFT}

# S
SPAWN_TIME = 1600

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s
TIMEOUT_LEVEL3 = 40000

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 90),
             'EnterName': (WIN_WIDTH / 2, 180),
             'Label': (WIN_WIDTH / 2, 170),
             'Name': (WIN_WIDTH / 2, 200),
             0: (WIN_WIDTH / 2, 200),
             1: (WIN_WIDTH / 2, 220),
             2: (WIN_WIDTH / 2, 240),
             3: (WIN_WIDTH / 2, 260),
             4: (WIN_WIDTH / 2, 280),
             5: (WIN_WIDTH / 2, 300),
             6: (WIN_WIDTH / 2, 320),
             7: (WIN_WIDTH / 2, 340),
             8: (WIN_WIDTH / 2, 360),
             9: (WIN_WIDTH / 2, 390),
             'ESC': (WIN_WIDTH / 2, 400)
             }