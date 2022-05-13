import pygame as pg
import random
import math
import time

# initialisation
pg.init()

# Create the screen:
screen = pg.display.set_mode((800, 600))

# Changing the title
pg.display.set_caption("MONSTERS ATTACK ")

# Changing the icon
icon = pg.image.load("monster_image.png")
pg.display.set_icon(icon)

# Background
backGround = pg.image.load("back_ground2.png")

# Adding the player
playerImage = pg.image.load("attacker.png")
positionXPlayer = 630
positionYPlayer = 450
playerYchange = 0
playerXchange = 0


def player(x, y):
    screen.blit(playerImage, (x, y))  # drawing the player on screen


# Adding the monsters
list_Monsters = [pg.image.load("monster_image.png"), pg.image.load("monster_image2.png"),
                 pg.image.load("monster_image3.png"), pg.image.load("monster_image4.png")]
MonsterImage = list_Monsters[random.randint(0, len(list_Monsters) - 1)]
positionXMonster = random.randint(50, 150)
positionYMonster = random.randint(20, 500)
monsterXChange = 1
monsterYChange = 1


def monster(x, y):
    screen.blit(MonsterImage, (x, y))


# Creating the bullets
bulletImage = pg.image.load("bullets.png")

positionXBullet = positionXPlayer
positionYBullet = 0
BulletXChange = 10
BulletYChange = 0
bulletState = "ready"  # Ready -> you can't see the bullet on the screen


# Fire -> you can see the bullet on the screen
def fireBullet(x, y):
    global bulletState
    bulletState = "Fire"
    screen.blit(bulletImage, (x + 20, y + 14.5))


def isCollision(bulletX, bulletY, monsterX, monsterY):
    distance = math.sqrt(math.pow(monsterX - bulletX, 2) + math.pow(monsterY - bulletY, 2))
    collisionOccured = False
    if distance < 27:
        collisionOccured = True

    return collisionOccured
score = 0

running = True
while running:  # We iterate through all the possible events. The window stays
    # opened until we close it(pg.event == QUIT
    # RGB --> RED - GREEN - BLUE
    # screen.fill((0,0,0))
    screen.blit(backGround, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                playerYchange = 5
            if event.key == pg.K_DOWN:
                playerYchange = -5
            #if event.key == pg.K_LEFT:
            #    playerXchange = 5
            #if event.key == pg.K_RIGHT:
            #    playerXchange = -5
            if event.key == pg.K_SPACE:
                positionYBullet = positionYPlayer
                positionXBullet = positionXPlayer
                fireBullet(positionXBullet, positionYBullet)

        if event.type == pg.KEYUP:
            if event.key == pg.K_UP or event.key == pg.K_DOWN or pg.K_LEFT or event.key == pg.K_RIGHT:
                playerYchange = 0
                playerXchange = 0

    positionYPlayer -= playerYchange
    positionXPlayer -= playerXchange
    if positionYPlayer <= 0:
        positionYPlayer = 0
    if positionYPlayer >= 538:
        positionYPlayer = 538
    if positionXPlayer >= 740:
        positionXPlayer = 740
    if positionXPlayer <= 545:
        positionXPlayer = 545

    positionYMonster += monsterYChange
    if positionYMonster >= 570:
        monsterYChange = -3
        positionXMonster += 50
    if positionYMonster <= 0:
        monsterYChange = 3
        positionXMonster += 50

    player(positionXPlayer, positionYPlayer)
    monster(positionXMonster, positionYMonster)
    if positionXBullet <= 0:
        positionXBullet = positionXPlayer
        bulletState = "ready"
    if bulletState == "Fire":
        fireBullet(positionXBullet, positionYBullet)
        positionXBullet -= BulletXChange
    # bullet(positionXBullet,positionYBullet)

    # collision
    collision = isCollision(positionXBullet, positionYBullet, positionXMonster, positionYMonster)
    if collision:
        bulletState = "ready"
        positionXBullet = positionXPlayer
        if MonsterImage == list_Monsters[0] or MonsterImage == list_Monsters[1]:
            score += 5
        else:
            score += 10
        positionXMonster = random.randint(50, 150)
        positionYMonster = random.randint(20, 500)
        print(score)
    pg.display.update()  # always include this line; serves to update the display(game window)
