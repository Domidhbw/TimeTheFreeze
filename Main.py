import pygame
from LevelEditor.listGenerator import LevelGenerator
from testOBJ import Player

pygame.init()
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()
running = True


#initialize class
level = LevelGenerator("LevelEditor/testLevel.txt",pygame.display.get_surface())
player = Player()
applyGravity = True

while running:
    #GET INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player.hasJump:
            player.rectangle.y -= 14000 * dt
            applyGravity = True
            player.hasJump = False
    if keys[pygame.K_a]:
        player.rectangle.x -= 300 * dt
    if keys[pygame.K_d]:
        player.rectangle.x += 300 * dt

    #GAMELOOP

    #FOR COLLISION LOOP THROUGH level.ground
    for collisions in level.ground:
        collisions.rectangle.update(collisions.rectangle.left,collisions.rectangle.top,level.tileScale[1],level.tileScale[0])
        if collisions.rectangle.colliderect(player.rectangle):
            print("collision")
            applyGravity = False    
        if collisions.rectangle.colliderect(player.groundCheck):
            player.hasJump = True


    if applyGravity:
        player.rectangle.y += player.downforce

    # RENDER YOUR GAME HERE
    for tile in level.level:
        tile.rectangle.update(tile.rectangle.left,tile.rectangle.top,level.tileScale[1],level.tileScale[0])
        tile.draw(screen)
    pygame.draw.rect(screen,"red",player.rectangle)

    pygame.display.flip()

    dt = clock.tick(60)/1000  # limits FPS to 60

pygame.quit()
