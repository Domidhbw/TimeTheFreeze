import pygame
from Level.levelManager import LevelManager
from player.player import Player
from collisionHandler import CollisionHandler
from superPower import doSuperPower
from Menu.menu import Menu

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True

#initialize class
background = pygame.image.load('./assets/Background.png').convert()
menu = Menu()
levelManager = LevelManager()
levelManager.createLevel()
levelManager.createCollisionMap()
player = Player(pygame.Vector2(400,50),5)
collision = CollisionHandler(player,levelManager)
collision.createKillTileList()
superPower = doSuperPower()

menu.main(screen)
levelManager.loadNewLevel(menu.selectedLevel)
levelManager.resetLevel()

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("darkgrey")
    #GAMELOOP  
    player.update(levelManager)
    collision.update(player,levelManager.collisionMap)
    levelManager.update(player)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        superPower.doIt(player,levelManager)

    #DRAW THE GAME
    screen.blit(background,(0,0)) 
    levelManager.drawLevel(screen)
    player.draw(screen)
    
    pygame.display.flip()

    dt = clock.tick(60)/1000  

pygame.quit()


