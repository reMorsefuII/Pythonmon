import time
import pygame
from pygame.math import clamp

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

pygame.mixer.music.load(addPath('backgroundMusic.mp3'))
pygame.mixer.music.set_volume(0.65)
pygame.mixer.music.play(-1)
damageEffect = pygame.mixer.Sound(addPath('damage.wav'))
damageEffect.set_volume(0.75)
victory = pygame.mixer.Sound(addPath('victory.mp3'))
victory.set_volume(0.75)

baseTextFont35 = pygame.font.Font(addPath("munro.ttf"), 35)
baseTextFont20 = pygame.font.Font(addPath("munro.ttf"), 20)
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
    "Move1Details": [(270, 70), (180, 500)],
    "Move2Name": [(270, 70), (510, 460)],
    "Move2Details": [(270, 70), (510, 500)],
    "Move3Name": [(270, 70), (180, 550)],
    "Move3Details": [(270, 70), (180, 590)],
    "Move4Name": [(270, 70), (510, 550)],
    "Move4Details": [(270, 70), (510, 590)],
    "EnemyHPOutline": [(350, 80), (325, 57)],
    "EnemyHP": [(340, 70), (325, 57)],
    "PlayerHPOutline": [(350, 80), (475, 323)],
    "PlayerHP": [(340, 70), (475, 323)],
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
playerSprite["Image"] = pygame.image.load(addPath(f"{player.Name}.png")).convert_alpha()
playerSprite["Rect"] = playerSprite["Image"].get_rect()
playerSprite["CurrentOffset"] = -425
enemySprite["Image"] = pygame.image.load(addPath(f"{enemy.Name}.png")).convert_alpha()
enemySprite["Rect"] = enemySprite["Image"].get_rect()
enemySprite["CurrentOffset"] = 1225

def drawBG():
    Window.fill((100, 255, 100))
    pygame.draw.ellipse(Window, (200, 200, 150), (525, 150, 250, 100)) #Enemy
    pygame.draw.ellipse(Window, (200, 200, 150), (25, 280, 250, 100)) #Player

def drawBottomBar(text=None):
    global baseText, FightBoxCheck, Moves, Back
    FightBoxCheck, Back = None, None
    pygame.draw.rect(Window, (200, 200, 150), (0, 400, 800, 200))
    pygame.draw.rect(Window, (150, 150, 100), (0, 400, 800, 10))
    if not (text is None):
        baseText = baseTextFont35.render(text, True, (0, 0, 0))
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
        drawRect((190, 190, 140), "Move1Inline")
        drawRect((190, 190, 140), "Move2Inline")
        drawRect((190, 190, 140), "Move3Inline")
        drawRect((190, 190, 140), "Move4Inline")
        Window.blit(preparedTexts["Back"][0], preparedRects["Back"])
        #Attack NAMES                                                                                                                                                                                                                                                                                                                                                     idiot. code: thebestgamemoneycantbuy
        Window.blit(baseTextFont35.render(player.Moves[0]["Name"], True, (0, 0, 0)), preparedRects["Move1Name"])
        Window.blit(baseTextFont35.render(player.Moves[1]["Name"], True, (0, 0, 0)), preparedRects["Move2Name"])
        Window.blit(baseTextFont35.render(player.Moves[2]["Name"], True, (0, 0, 0)), preparedRects["Move3Name"])
        Window.blit(baseTextFont35.render(player.Moves[3]["Name"], True, (0, 0, 0)), preparedRects["Move4Name"])

        #Attack DETAILS
        Window.blit(baseTextFont20.render(f"Power: {player.Moves[0]["Power"]}    Accuracy: {player.Moves[0]["Accuracy"]}", True, (0, 0, 0)), preparedRects["Move1Details"])
        Window.blit(baseTextFont20.render(f"Power: {player.Moves[1]["Power"]}    Accuracy: {player.Moves[1]["Accuracy"]}", True,(0, 0, 0)), preparedRects["Move2Details"])
        Window.blit(baseTextFont20.render(f"Power: {player.Moves[2]["Power"]}    Accuracy: {player.Moves[2]["Accuracy"]}", True,(0, 0, 0)), preparedRects["Move3Details"])
        Window.blit(baseTextFont20.render(f"Power: {player.Moves[3]["Power"]}    Accuracy: {player.Moves[3]["Accuracy"]}", True,(0, 0, 0)), preparedRects["Move4Details"])

        Back = preparedRects["Back"]

    Window.blit(baseText, (20, 425))

def drawEnemyHealthbar(healthSet=None):
    drawRect((150, 150, 100), "EnemyHPOutline") #Outline
    drawRect((190, 190, 140), "EnemyHP")

    if healthSet is None:
        healthSet = enemy.Health
    Window.blit(baseTextFont35.render(enemy.Name, True, (0, 0, 0)), (165, 24))  # Name
    Window.blit(baseTextFont20.render(f"{clamp(healthSet, 0, enemy.MaxHealth)}/{enemy.MaxHealth}", True, (0, 0, 0)), (165, 57))


def drawPlayerHealthbar(healthSet=None):
    drawRect((150, 150, 100), "PlayerHPOutline")  # Outline
    drawRect((190, 190, 140), "PlayerHP")

    if healthSet is None:
        healthSet = player.Health
    # Texts
    Window.blit(baseTextFont35.render(player.Name, True, (0, 0, 0)), (315, 290))  # Name
    Window.blit(baseTextFont20.render(f"{clamp(healthSet, 0, player.MaxHealth)}/{player.MaxHealth}", True, (0, 0, 0)), (315, 325))


def runMessage(message : str):
    for x in range(len(message)):
        drawBottomBar(message[:x])
        pygame.display.flip()
        Clock.tick(40)
    drawBottomBar(message)
    pygame.display.flip()

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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if status == "DisplayChoice" and not (FightBoxCheck is None) and FightBoxCheck.collidepoint(pygame.mouse.get_pos()):
                status = "DisplayMoves"
                print("fuck yeah")
                break
            elif status == "DisplayMoves":
                if not (Back is None):
                    if Back.collidepoint(pygame.mouse.get_pos()):
                        status = "DisplayChoice"
                        break
                    else:
                        for index, mrect in enumerate(Moves):
                            if mrect.collidepoint(pygame.mouse.get_pos()):
                                #Player Move
                                status = "RunMessage"
                                runMessage(f"Your {player.Name} used {player.Moves[index]["Name"]}!")
                                time.sleep(0.45)
                                pygame.mixer.find_channel().play(damageEffect)
                                currentHP = enemy.Health
                                Clock.tick(1)
                                if enemy.takeDamage(player.Moves[index]):
                                    print(enemy.Health)
                                    changeHP = math.floor(player.Moves[index]["Power"]/20)
                                    for i in range(20):
                                        if changeHP == 0:
                                            if i % 2 == 0:
                                                drawEnemyHealthbar(math.floor(currentHP-0.5*i))
                                        else:
                                            drawEnemyHealthbar(currentHP-changeHP*i)
                                        pygame.display.flip()
                                        Clock.tick(45)
                                    drawEnemyHealthbar()
                                    pygame.display.flip()
                                else:
                                    runMessage(f"{player.Name} missed their attack!")
                                Clock.tick(1)

                                if enemy.Health == 0:
                                    pygame.mixer.music.fadeout(1000)
                                    Clock.tick(5)
                                    victory.play()
                                    runMessage(f"Your {player.Name} won the fight!")
                                    Clock.tick(0.085)
                                    victory.fadeout(1500)
                                    Clock.tick(0.65)
                                    status = "Quit"
                                    break
                                #Enemy Move

                                randomMove = enemy.Moves[random.randint(0, 3)]
                                runMessage(f"The enemy {enemy.Name} used {randomMove["Name"]}!")
                                time.sleep(0.45)
                                pygame.mixer.find_channel().play(damageEffect)
                                currentHP = player.Health
                                Clock.tick(1)
                                if player.takeDamage(randomMove):
                                    changeHP = math.floor(randomMove["Power"] / 20)
                                    for i in range(20):
                                        if changeHP == 0:
                                            if i % 2 == 0:
                                                drawPlayerHealthbar(math.floor(currentHP-0.5*i))
                                        else:
                                            drawPlayerHealthbar(currentHP-changeHP*i)
                                        pygame.display.flip()
                                        Clock.tick(45)
                                    drawPlayerHealthbar()
                                    pygame.display.flip()
                                else:
                                    runMessage(f"{enemy.Name} missed their attack!")
                                Clock.tick(1)

                                if player.Health == 0:
                                    pygame.mixer.music.fadeout(3000)
                                    Clock.tick(5)
                                    runMessage(f"You lost...")
                                    Clock.tick(0.2)
                                    status = "Quit"
                                    break

                                status = "DisplayChoice"

    drawBG()
    drawBottomBar()
    if status == "Start":
        intro()
        status = "DisplayChoice"
    Window.blit(playerSprite["Image"], playerSprite["Rect"])
    Window.blit(enemySprite["Image"], enemySprite["Rect"])
    drawEnemyHealthbar()
    drawPlayerHealthbar()
    pygame.display.flip()
    Clock.tick(60)