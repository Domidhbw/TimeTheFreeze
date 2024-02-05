import pygame
from Level.levelManager import LevelManager
from player.player import Player
from collisionHandler import CollisionHandler
from superPower import doSuperPower

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True

#initialize class
levelManager = LevelManager()
levelManager.createLevel()
levelManager.createCollisionMap()
player = Player(pygame.Vector2(400,50),20)
collision = CollisionHandler(player,levelManager.collisionMap)
superPower = doSuperPower(levelManager.collisionMap,levelManager.level)

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
    player.update()
    collision.update(player,levelManager.collisionMap)
    levelManager.update(player)


    #DRAW THE GAME
    levelManager.drawLevel(screen)
    pygame.draw.rect(screen,player.color,player.rect)
    pygame.display.flip()

    dt = clock.tick(60)/1000  

pygame.quit()
