import pygame
from Level.levelManager import LevelManager
from player.player import Player
from collisionHandler import CollisionHandler
from superPower import doSuperPower
from Menu.menu import Menu
from music import music
from Menu.escapeMenu import EscapeMenu

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
escape = 'escape'

#Music Settings
musicHandler = music.MusicHandler()

#initialize classes
escapeMenu = EscapeMenu(musicHandler)
background = pygame.image.load('./assets/Background.png').convert()
menu = Menu()
player = Player(pygame.Vector2(400,90),300,musicHandler)
levelManager = LevelManager(player)
levelManager.createLevel()
levelManager.createCollisionMap()
collision = CollisionHandler(player,levelManager)
collision.createKillTileList()
superPower = doSuperPower(musicHandler)


while running:
    #GET INPUT
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        elif gameState == levelSelection:
            #input handling for level selection menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameState = menu.handleMouse(pygame.mouse.get_pos(),levelManager,player)
        elif gameState == playing:
            if keys[pygame.K_w]:
                superPower.doIt(player,levelManager)
            if keys[pygame.K_ESCAPE]:
                gameState = escape
        elif gameState == escape:
            if event.type == pygame.MOUSEBUTTONDOWN:
                gameState = escapeMenu.handleInput(pygame.mouse.get_pos(),player,levelManager)
        elif gameState == 'quit':
            running = False

    if gameState == levelSelection:
        musicHandler.playTrack(1,False)
        menu.draw(screen,window)
        pygame.display.flip()
        continue

    if gameState == escape:
        escapeMenu.drawEscapeMenu(screen,window)
        pygame.display.flip()
        continue

    if gameState == playing:
        musicHandler.playTrack(0,False)
        screen.fill("darkgrey")
        #GAMELOOP  
        player.update(levelManager)
        levelManager.update(player,dt)
        collision.update(player,levelManager.collisionMap,dt)

        #DRAW THE GAME
        screen.blit(background,(0,0)) 
        levelManager.drawLevel(screen)
        player.draw(screen)
        
        scaled_surface = pygame.transform.scale(screen, (windowWidth, windowHeight))

        window.blit(scaled_surface,(0,0))
        
        pygame.display.flip()

    musicHandler.updateMusic()
    dt = clock.tick(60)/1000  

pygame.quit()

