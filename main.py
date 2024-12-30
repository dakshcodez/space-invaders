import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

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
enemyImg = pygame.image.load('enemy.png')
enemyX = 370
enemyY = 50
enemyY_change = 0

def player(x,y):
    screen.blit(playerImg,(x,y))     # Puts the player on the screen

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

# Game Loop
running = True
while running:

    # R,G,B Values
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.25
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX = 736

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()