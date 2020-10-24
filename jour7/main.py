import pygame
import sys
import numpy as np
from pygame.locals import QUIT
import time

height = 540
width = 540
white = (255, 255, 255)
black = (0, 0, 0)
user1 = "human"
user = None
user2 = None
positionlist = []
stepslistia = []
steplisthuman = []
boardcalcul = [[0 for x in range(3)] for y in range(3)]
# Initialise screen
pygame.init()
screen = pygame.display.set_mode((width+60, height+60))
pygame.display.set_caption('TicTacToe1337')
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
# Fill background
background = pygame.Surface(screen.get_size())


def startscreen():
    global background
    pygame.init()
    screen = pygame.display.set_mode((width+60, height+60))
    background = background.convert()
    background.fill(white)
    # Display button text
    font = pygame.font.Font(None, 36)
    text1 = font.render("With AI", 1, black)
    text2 = font.render("With Friend", 1, black)
    textpos1 = text1.get_rect(center=(80, 600-30))
    textpos2 = text1.get_rect(center=(270, 600-30))
    background.blit(text1, textpos1)
    background.blit(text2, textpos2)
    # drawing horizontal lines
    pygame.draw.line(background, black, (30+(width/3), 0),
                     (30+(width/3), height+60), 5)
    pygame.draw.line(background, black, (30+(2*width/3), 0),
                     (30+(2*width/3), height+60), 5)
    # drawing vertical lines
    pygame.draw.line(background, black, (30, width/3), (570, width/3), 5)
    pygame.draw.line(background, black, (30, 2*width/3), (570, 2*width/3), 5)
    pygame.draw.line(background, black, (0, 540), (600, 540), 5)
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.update()
    pygame.display.flip()


def winner():
    global boardcalcul, background, user2
    font = pygame.font.Font(None, 48)
    User1 = font.render("WINNER IS USER 1", 5, black)
    if user2 == "comp":
        message = "AI"
    else:
        message = "User2"
    User2 = font.render(f"WINNER IS {message}", 5, black)
    draw = font.render("DRAW", 5, black)
    columsumlist = np.sum(boardcalcul, axis=0)
    columsumlist1 = np.sum(boardcalcul, axis=1)
    columsumlist = np.concatenate((columsumlist, columsumlist1))
    columsumlist = list(columsumlist)
    b = np.asarray(boardcalcul)
    b = np.trace(b)
    columsumlist.append(b)
    c = boardcalcul[0][2]+boardcalcul[1][1]+boardcalcul[2][0]
    columsumlist.append(c)
    for i in columsumlist:
        if i == 9:
            background = background.convert()
            background.fill(white)
            Xpos = User1.get_rect(center=(300, 300))
            background.blit(User1, Xpos)
            screen.blit(background, (0, 0))
            pygame.display.update()
            print("User 1 wins")
            time.sleep(2)
            gamereset()
        elif i == 15:
            background = background.convert()
            background.fill(white)
            Xpos = User2.get_rect(center=(300, 300))
            background.blit(User2, Xpos)
            screen.blit(background, (0, 0))
            pygame.display.update()
            print("User 2 wins")
            time.sleep(2)
            gamereset()
        elif len(positionlist) == 9:
            background = background.convert()
            background.fill(white)
            Xpos = draw.get_rect(center=(300, 300))
            background.blit(draw, Xpos)
            screen.blit(background, (0, 0))
            pygame.display.update()
            print("Draw")
            time.sleep(2)
            gamereset()

        else:
            screen.blit(background, (0, 0))
            pygame.display.update()
            continue


def ia():
    global background, boardcalcul, positionlist, stepslistia, steplisthuman, user, user2
    if user2 == "comp" and user == user2:
        rowsumlist = list(np.sum(boardcalcul, axis=1))
        colsumlist = list(np.sum(boardcalcul, axis=0))
        diag = boardcalcul[0][0]+boardcalcul[1][1]+boardcalcul[2][2]
        diag1 = boardcalcul[0][2]+boardcalcul[1][1]+boardcalcul[2][0]
        boardcalcul = np.array(boardcalcul)
        boardcalculT = np.transpose(boardcalcul)
        row = None
        col = None
        if [1, 1] not in positionlist:
            row = 1
            col = 1
        elif len(positionlist) == 1:
            row = 0
            col = 0
        elif 10 in rowsumlist:
            row = rowsumlist.index(10)
            col = list(boardcalcul[row]).index(0)
        elif 10 in colsumlist:
            col = colsumlist.index(10)
            row = list(boardcalculT[col]).index(0)
        elif [1, 1] in stepslistia and diag == 10:
            if [0, 0] in stepslistia:
                row = 2
                col = 2
            else:
                row = 0
                col = 0
        elif [1, 1] in stepslistia and diag1 == 10:
            if [0, 2] in stepslistia:
                row = 2
                col = 0
            else:
                row = 0
                col = 2
        elif 6 in rowsumlist:
            row = rowsumlist.index(6)
            print(boardcalcul[row])
            col = list(boardcalcul[row]).index(0)
        elif 6 in colsumlist:
            col = colsumlist.index(6)
            print(boardcalcul[col])
            row = list(boardcalculT[col]).index(0)
        elif [1, 1] in steplisthuman and diag == 6:
            if [0, 0] in steplisthuman:
                row = 2
                col = 2
            else:
                row = 0
                col = 0
        elif [1, 1] in steplisthuman and diag1 == 6:
            if [0, 2] in steplisthuman:
                row = 2
                col = 0
            else:
                row = 0
                col = 2
        elif 3 in rowsumlist:
            row = rowsumlist.index(3)
            col = list(boardcalcul[row]).index(0)
        elif 3 in colsumlist:
            col = colsumlist.index(3)
            row = list(boardcalculT[col]).index(0)

        iaposition = [row, col]
        positionlist.append(iaposition)
        screen.blit(background, (0, 0))
        pygame.display.update()
        printXO(row, col)


def printXO(row, col):
    global background, user, user1, user2, boardcalcul, steplisthuman
    posx = None
    posy = None
    font = pygame.font.Font(None, 150)
    XO = font.render("X", 5, black)
    OX = font.render("O", 5, black)
    if row == 0:
        posy = 90
    elif row == 1:
        posy = 270
    else:
        posy = 450
    if col == 0:
        posx = 120
    elif col == 1:
        posx = 300
    else:
        posx = 480
    if(user == user1):
        Xpos = XO.get_rect(center=(posx, posy))
        steplisthuman.append([row, col])
        background.blit(XO, Xpos)
        boardcalcul[row][col] = 3
        user = user2
        winner()
        screen.blit(background, (0, 0))
        pygame.display.update()
        if user2 == "human2":
            mouseclick()
        else:
            ia()

    else:
        Opos = OX.get_rect(center=(posx, posy))
        background.blit(OX, Opos)
        boardcalcul[row][col] = 5
        stepslistia.append([row, col])
        user = user1
        winner()
        screen.blit(background, (0, 0))
        pygame.display.update()
        mouseclick()


def player():
    global user, user1, user2
    x, y = pygame.mouse.get_pos()
    font = pygame.font.Font(None, 36)
    message = None
    if user2 == None:
        if x < 210 and y > 540:
            user = user1
            user2 = "comp"
            message = "With AI *"

        elif 210 < x < 390 and y > 540:
            user = user1
            user2 = "human2"
            message = "With Friend *"
    text3 = font.render(message, 1, black)
    textpos3 = text3.get_rect(center=(500, 600-30))
    background.blit(text3, textpos3)
    screen.blit(background, (0, 0))
    pygame.display.update()
    mouseclick()


def mouseclick():
    global positionlist, user2
    x, y = pygame.mouse.get_pos()
    if user2 != None:
        if x > 30 and y < 540:
            x = (x-30)//180
            y = y//180
            row = y
            col = x
            mouseposition = [row, col]
            if mouseposition in positionlist:
                row = None
                col = None
            else:
                positionlist.append(mouseposition)
            if row != None:
                printXO(row, col)


def gamereset():
    global boardcalcul, positionlist, user, user1, steplisthuman, stepslistia, user2
    positionlist = []
    steplisthuman = []
    stepslistia = []
    user1 = "human"
    user = user1
    user2 = None
    boardcalcul = [[0 for x in range(3)] for y in range(3)]
    pygame.init()
    startscreen()


startscreen()
# Event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player()
    pygame.display.update()
    FramePerSec.tick(FPS)
