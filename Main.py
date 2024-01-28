import pygame
from LevelEditor.level import LevelGenerator
from player.player import Player
from collisionHandler import CollisionHandler

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True


#initialize class
level = LevelGenerator("LevelEditor/testLevel.txt",pygame.display.get_surface())
player = Player(50,50,5)
collision = CollisionHandler(player,level.level)

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")

    #GAMELOOP

    player.update()
    collision.update(player,level.level)
    level.drawLevel(screen)

    pygame.draw.rect(screen,"red",player.rect)
    pygame.display.flip()

    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()
