import pygame
from Level.levelManager import LevelManager
from player.player import Player
from collisionHandler import CollisionHandler
from superPower import doSuperPower
from Menu.menu import Menu
from saveManager.saveManager import SaveManager
from music import music

pygame.init()

musicHandler = music.MusicHandler()
musicHandler.playMusic()


baseWidth, baseHeight = 1800,900
windowWidth, windowHeight = pygame.display.Info().current_w,pygame.display.Info().current_h

window = pygame.display.set_mode((windowWidth,windowHeight))
screen = pygame.Surface((baseWidth,baseHeight))
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True

#initialize class
background = pygame.image.load('./assets/Background.png').convert()
menu = Menu(windowWidth,windowHeight)
svManager = SaveManager()
levelManager = LevelManager(svManager)
levelManager.createLevel()
levelManager.createCollisionMap()
player = Player(pygame.Vector2(400,90),300)
collision = CollisionHandler(player,levelManager)
collision.createKillTileList()
superPower = doSuperPower()


levelManager.loadNewLevel(1)
levelManager.resetLevel()

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("darkgrey")
    #GAMELOOP  
    player.update(levelManager)
    levelManager.update(player,dt)
    collision.update(player,levelManager.collisionMap,dt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        superPower.doIt(player,levelManager)

    #DRAW THE GAME
    screen.blit(background,(0,0)) 
    levelManager.drawLevel(screen)
    player.draw(screen)

    scaled_surface = pygame.transform.scale(screen, (windowWidth, windowHeight))

    window.blit(scaled_surface,(0,0))

    
    pygame.display.flip()

    dt = clock.tick(60)/1000  

pygame.quit()
