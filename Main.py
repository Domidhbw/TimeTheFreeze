import pygame
from LevelEditor.listGenerator import LevelGenerator
from player.player import Player

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
running = True


#initialize class
level = LevelGenerator("LevelEditor/testLevel.txt",pygame.display.get_surface())
player = Player(50,50,150)
applyGravity = True

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #FOR COLLISION LOOP THROUGH level.ground
    for collisions in level.ground:
        if collisions.rectangle.colliderect(player.groundCheck):
            player.applyGravity = False
            player.hasJump = True
        if collisions.rectangle.colliderect(player.rightCheck):
            player.rightHit = True
        if collisions.rectangle.colliderect(player.leftCheck):
            player.leftHit = True


        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.jump_pressed = True
    else:
        player.jump_pressed = False
    if keys[pygame.K_a]:
        player.right_pressed = True
    else:
        player.right_pressed = False
    if keys[pygame.K_d]:
        player.left_pressed = True
    else:
        player.left_pressed = False

    player.update(dt)
    #GAMELOOP

    # RENDER YOUR GAME HERE
    for tile in level.level:
        tile.draw(screen)
    pygame.draw.rect(screen,"red",player.rect)
    pygame.draw.rect(screen,"blue",player.rightCheck)
    pygame.draw.rect(screen,"blue",player.leftCheck)
    pygame.draw.rect(screen,"blue",player.upperCheck)
    pygame.draw.rect(screen,"blue",player.groundCheck)

    pygame.display.flip()

    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()
