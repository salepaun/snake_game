# Snake Game!

import pygame
import sys
import random
import time

# Check for initializing errors
check_errors = pygame.init()  # initializes all pygame modules
# (6, 0)
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized")

# Play surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game!')

# Colors
red = pygame.Color(255, 0, 0)  # game over
green = pygame.Color(0, 255, 0)  # snake
black = pygame.Color(0, 0, 0)  # score
white = pygame.Color(255, 255, 255)  # background
brown = pygame.Color(165, 42, 42)  # food

# FPS controller
fpsController = pygame.time.Clock()

# Important variables
snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

direction = 'RIGHT'
changeTo = direction

score = 0


def exitGame():
    pygame.quit()  # pygame exit
    sys.exit(0)  # console exit


# Game over function
def gameOver():
    myFont = pygame.font.SysFont('Monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    playSurface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(3)
    exitGame()


def showScore(choice=1):
    myFont = pygame.font.SysFont('Monaco', 24)
    Ssurf = myFont.render('Score :  {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice != 1:
        Srect.midtop = (360, 120)
    else:
        Srect.midtop = (80, 10)
    playSurface.blit(Ssurf, Srect)


# Game logic
while 1:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            exitGame()
        elif evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_RIGHT or evnt.key == ord('d'):
                changeTo = 'RIGHT'
            if evnt.key == pygame.K_LEFT or evnt.key == ord('a'):
                changeTo = 'LEFT'
            if evnt.key == pygame.K_UP or evnt.key == ord('w'):
                changeTo = 'UP'
            if evnt.key == pygame.K_DOWN or evnt.key == ord('s'):
                changeTo = 'DOWN'
            if evnt.key == pygame.K_ESCAPE:
                exitGame()

    # validation of direction
    if changeTo == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeTo == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeTo == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeTo == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        foodSpawn = False
        score +=1
    else:
        snakeBody.pop()
    if not foodSpawn:
        foodPos = [random.randrange(10, 720, 10), random.randrange(10, 460, 10)]
        foodSpawn = True

    playSurface.fill(white)

    for pos in snakeBody:
        pygame.draw.rect(playSurface, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    # Bounds
    if snakePos[0] > 710 or snakePos[0] < 0 or snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    # Self hit
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()
    showScore()
    pygame.display.flip()

    fpsController.tick(24)


# pyinstaller
# menu
# sounds
# icon
# custom sprites
