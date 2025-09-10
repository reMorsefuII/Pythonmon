import string

import pygame
import entity
import random
import math
import sys
import os


status = "Start"

def addPath(r_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, r_path)

# Display initialization
pygame.init()
pygame.display.set_caption('Pythonmon')
pygame.display.set_icon(pygame.image.load(addPath('icon.png')))
Window = pygame.display.set_mode((800, 600))
Clock = pygame.time.Clock()

sound = pygame.mixer.Sound(addPath('backgroundMusic.mp3'))
sound.set_volume(0.65)
pygame.mixer.find_channel().play(sound, -1)

baseTextFont35 = pygame.font.Font(addPath("munro.ttf"), 35)
baseTextFont70 = pygame.font.Font(addPath("munro.ttf"), 70)
secretTextFont = pygame.font.Font(addPath("wingding.ttf"), 35)

preparedTexts = {
    "Fight": [baseTextFont70.render("Fight", True, (0,0,0)), (400, 525)],
    "Back": [baseTextFont35.render("Back >", True, (0,0,0)), (745, 435)]
}
prepreparedRects = {
    "FightBox": [(250, 100), (400, 525)],
    "FightBoxOutline": [(260, 110), (400, 525)],
    "Move1": [(300, 80), (180, 460)],
    "Move2": [(300, 80), (510, 460)],
    "Move3": [(300, 80), (180, 550)],
    "Move4": [(300, 80), (510, 550)],
    "Move1Inline": [(290, 70), (180, 460)],
    "Move2Inline": [(290, 70), (510, 460)],
    "Move3Inline": [(290, 70), (180, 550)],
    "Move4Inline": [(290, 70), (510, 550)],
    "Move1Name": [(270, 70), (180, 460)],
    "Move2Name": [(270, 70), (510, 460)],
    "Move3Name": [(270, 70), (180, 550)],
    "Move4Name": [(270, 70), (510, 550)],
}
preparedRects, Moves = dict(), list()

FightBoxCheck, Back = None, None

for i, v in preparedTexts.items():
    rect = v[0].get_rect()
    rect.center = v[1]
    preparedRects[i] = rect
for i, v in prepreparedRects.items():
    rect = pygame.Rect(v[1], v[0])
    rect.center = v[1]
    preparedRects[i] = rect


def drawRect(color, rectName : str):
    return pygame.draw.rect(Window, color, preparedRects[rectName])

baseText = baseTextFont35.render("how the fuck are you reading this you cheater", True, (0, 0, 0))
# If you're reading the internal source code for the decoded messages you're a fucking bum
secretTexts = [secretTextFont.render("isitsnoopfrog? snoop frog frog snoop", True, (0, 0, 0)), secretTextFont.render("99 105 112 104 101 114 32 110 101 114 100", True, (0, 0, 0)), secretTextFont.render("have you ever puthed around before", True, (0, 0, 0))]

player, enemy = entity.Entity(entity.names[random.randint(0, len(entity.names)-1)]), entity.Entity(entity.names[random.randint(0, len(entity.names)-1)])
playerSprite, enemySprite = dict(), dict()
playerSprite["Image"] = pygame.image.load(addPath("testshit.jpeg")).convert_alpha()
playerSprite["Rect"] = playerSprite["Image"].get_rect()
playerSprite["CurrentOffset"] = -400
enemySprite["Image"] = pygame.image.load(addPath("snoopfrog.png")).convert_alpha()
enemySprite["Rect"] = enemySprite["Image"].get_rect()
enemySprite["CurrentOffset"] = 1200

def drawBG():
    Window.fill((100, 255, 100))
    pygame.draw.ellipse(Window, (200, 200, 150), (500, 150, 250, 100))
    pygame.draw.ellipse(Window, (200, 200, 150), (50, 280, 250, 100))

def drawBottomBar():
    global baseText, FightBoxCheck, Moves, Back
    FightBoxCheck, Back = None, None
    pygame.draw.rect(Window, (200, 200, 150), (0, 400, 800, 200))
    pygame.draw.rect(Window, (150, 150, 100), (0, 400, 800, 10))
    if status == "Start":
        baseText = baseTextFont35.render(f"Your {player.Name} has challenged {enemy.Name}!", True, (0, 0, 0))
    elif status == "DisplayChoice":
        baseText = baseTextFont35.render(f"What will {player.Name} do?", True, (0, 0, 0))
        FightBoxCheck = drawRect((120, 120, 70), "FightBoxOutline")
        drawRect((150, 150, 100), "FightBox")
        Window.blit(preparedTexts["Fight"][0], preparedRects["Fight"])
    elif status == "DisplayMoves":
        baseText = baseTextFont35.render("", True, (0, 0, 0))
        M1, M2, M3, M4 = drawRect((150, 150, 100), "Move1"), drawRect((150, 150, 100), "Move2"), drawRect((150, 150, 100), "Move3"), drawRect((150, 150, 100), "Move4")
        Moves.clear()
        Moves.extend([M1, M2, M3, M4])
        drawRect((200, 200, 150), "Move1Inline")
        drawRect((200, 200, 150), "Move2Inline")
        drawRect((200, 200, 150), "Move3Inline")
        drawRect((200, 200, 150), "Move4Inline")
        Window.blit(preparedTexts["Back"][0], preparedRects["Back"])
        #Attack NAMES
        Window.blit(baseTextFont35.render(player.Moves[0]["Name"], True, (0, 0, 0)), preparedRects["Move1Name"])
        Window.blit(baseTextFont35.render(player.Moves[1]["Name"], True, (0, 0, 0)), preparedRects["Move2Name"])
        Window.blit(baseTextFont35.render(player.Moves[2]["Name"], True, (0, 0, 0)), preparedRects["Move3Name"])
        Window.blit(baseTextFont35.render(player.Moves[3]["Name"], True, (0, 0, 0)), preparedRects["Move4Name"])
        Back = preparedRects["Back"]

    Window.blit(baseText, (20, 425))

def drawHealthbars():
    print("hi")

def intro():
    for x in range(145):
        drawBG()
        playerSprite["CurrentOffset"] = playerSprite["CurrentOffset"] + 4
        enemySprite["CurrentOffset"] = enemySprite["CurrentOffset"] - 4
        playerSprite["Rect"].center = (playerSprite["CurrentOffset"], 230)
        enemySprite["Rect"].center = (enemySprite["CurrentOffset"], 100)
        Window.blit(playerSprite["Image"], playerSprite["Rect"])
        Window.blit(enemySprite["Image"], enemySprite["Rect"])
        drawBottomBar()
        pygame.display.flip()
        Clock.tick(60)

while status != "Quit":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = "Quit"
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if status == "DisplayChoice" and not (FightBoxCheck is None) and FightBoxCheck.collidepoint(pygame.mouse.get_pos()):
                status = "DisplayMoves"
                print("hell yeah")
                break
            elif status == "DisplayMoves":
                if not (Back is None) and Back.collidepoint(pygame.mouse.get_pos()):
                    status = "DisplayChoice"
                    break
    drawBG()
    drawBottomBar()
    if status == "Start":
        intro()
        status = "DisplayChoice"
    Window.blit(playerSprite["Image"], playerSprite["Rect"])
    Window.blit(enemySprite["Image"], enemySprite["Rect"])
    pygame.display.flip()
    Clock.tick(60)