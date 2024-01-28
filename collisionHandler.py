import pygame

class CollisionHandler():
    def __init__(self,player,collisionMap) -> None:
        self.player = player
        self.collisionMap = collisionMap

    def update(self,player,collisionMap):
        self.player = player
        self.collisionMap = collisionMap
        self.verticalMovementCollisions()
        self.horizontalMovementCollisions()


    def horizontalMovementCollisions(self):
        self.player.rect.x += self.player.direction.x * self.player.speed         
        for tile in self.collisionMap:
            if tile.rectangle.colliderect(self.player.rect):
                if self.player.direction.x < 0:
                    pass
                    self.player.rect.left = tile.rectangle.right
                elif self.player.direction.x > 0:
                    pass
                    self.player.rect.right = tile.rectangle.left
    
    def verticalMovementCollisions(self):
        self.player.applyGravity()
        for tile in self.collisionMap:
            if tile.rectangle.colliderect(self.player.rect):
                print(self.player.direction.y)
                if self.player.direction.y > 0:
                    self.player.direction.y = 0
                    self.player.rect.bottom = tile.rectangle.top
                elif self.player.direction.y < 0:
                    self.player.direction.y = 0
                    self.player.rect.top = tile.rectangle.bottom





