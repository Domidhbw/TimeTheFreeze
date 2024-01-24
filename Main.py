import pygame
from LevelEditor.listGenerator import LevelGenerator

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True


#initialize class
level = LevelGenerator("LevelEditor/testLevel.txt",pygame.display.get_surface())



while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    #GAMELOOP


    # RENDER YOUR GAME HERE
    for tile in level.level:
        tile.rectangle.update(tile.rectangle.left,tile.rectangle.top,level.tileScale[1],level.tileScale[0])
        tile.draw(screen)


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
