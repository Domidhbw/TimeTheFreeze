import pygame
from listGenerator import LevelGenerator

pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
running = True

level = LevelGenerator("testLevel.txt",pygame.display.get_surface())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    for tile in level.level:
        tile.rectangle.update(tile.rectangle.left,tile.rectangle.top,level.tileScale[1],level.tileScale[0])
        tile.draw(screen)
    # RENDER YOUR GAME HERE

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
