import pygame

class CollisionHandler():
    def __init__(self,player,levelManager) -> None:
        self.player = player
        self.collisionMap = levelManager.collisionMap
        self.levelManager = levelManager

    def update(self,player,collisionMap):
        self.player = player
        self.collisionMap = collisionMap
        self.horizontalMovementCollisions()
        self.verticalMovementCollisions()

    def horizontalMovementCollisions(self):
        self.player.applyFriction()
        self.player.move()         
        for tile in self.collisionMap:
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.x < 0:
                    self.player.rect.left = tile.rect.right
                elif self.player.direction.x > 0:
                    self.player.rect.right = tile.rect.left
                if tile.char == 'f':
                    self.levelManager.loadNewLevel()
                    self.levelManager.resetLevel()

    
    def verticalMovementCollisions(self):
        self.player.applyGravity()
        for tile in self.collisionMap:
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0:
                    self.player.direction.y = 0
                    self.player.rect.bottom = tile.rect.top
                    self.player.hasJump = True
                elif self.player.direction.y < 0:
                    self.player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0






