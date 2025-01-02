import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('bg.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 360
playerY = 480
playerX_change = 0

# Enemy
enemyImg =[]
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 5
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.25)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1.3
bullet_state = "ready"

score = 0

def player(x,y):
    screen.blit(playerImg,(x,y))     # Puts the player on the screen

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16 ,y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # R,G,B Values
    screen.fill((0,0,0))

    # Background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Boundary Check
    playerX += playerX_change
    
    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX = 736

    for i in range(no_of_enemies):
        enemyX[i] +=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state = "ready"
            score +=1
            print(score)
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)
        
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change

    player(playerX,playerY)
    
    pygame.display.update()