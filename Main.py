import pygame
from Level.levelManager import LevelManager
from player.player import Player
from collisionHandler import CollisionHandler
from superPower import doSuperPower
from Menu.menu import Menu
from saveManager.saveManager import SaveManager
from music import music

pygame.init()

#Window Settings
baseWidth, baseHeight = 1800,900
windowWidth, windowHeight = 700,500
windowWidth, windowHeight = pygame.display.Info().current_w,pygame.display.Info().current_h
window = pygame.display.set_mode((windowWidth,windowHeight))
screen = pygame.Surface((baseWidth,baseHeight))

#pygame Settings
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True

#Level Logic settings
playing = 'playing'
levelSelection = 'levelSelection'
paused = 'paused'
gameState = levelSelection

#initialize classes
background = pygame.image.load('./assets/Background.png').convert()
menu = Menu()
levelManager = LevelManager()
levelManager.createLevel()
levelManager.createCollisionMap()
player = Player(pygame.Vector2(400,90),300)
collision = CollisionHandler(player,levelManager)
collision.createKillTileList()
superPower = doSuperPower()

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif gameState == levelSelection:
            #input handling for level selection menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameState = menu.handleMouse(pygame.mouse.get_pos(),levelManager)
        elif gameState == playing:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                superPower.doIt(player,levelManager)

    if gameState == levelSelection:
        menu.draw(screen,window)
        pygame.display.flip()
        continue

    if gameState == playing:
        screen.fill("darkgrey")
        #GAMELOOP  
        player.update(levelManager)
        levelManager.update(player)
        collision.update(player,levelManager.collisionMap)

        #DRAW THE GAME
        screen.blit(background,(0,0)) 
        levelManager.drawLevel(screen)
        player.draw(screen)

        scaled_surface = pygame.transform.scale(screen, (windowWidth, windowHeight))

        window.blit(scaled_surface,(0,0))
        
        pygame.display.flip()

    dt = clock.tick(60)/1000  

pygame.quit()
