import pygame
from LevelEditor.level import LevelGenerator
from player.player import Player
from collisionHandler import CollisionHandler
from superPower import doSuperPower

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True

#initialize class
level = LevelGenerator("LevelEditor/testLevel.txt")
player = Player(pygame.Vector2(400,50),5)
collision = CollisionHandler(player,level.ground)
superPower = doSuperPower(level.ground,level.level)

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        superPower.doIt(player)
   
    #GAMELOOP
    level.update(screen,player)


    player.update()
    collision.update(player,level.ground)


    #DRAW THE GAME
    pygame.draw.rect(screen,player.color,player.rect)
    pygame.display.flip()



    dt = clock.tick(60)/1000  

pygame.quit()
