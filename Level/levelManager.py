import pygame
from .level import *
from .tileManager import TileManager

class LevelManager:
    def __init__(self) -> None:
        self.LevelData = level_map
        self.tileManager = TileManager()
        self.level = list()
        self.shift = pygame.Vector2()
        self.collisionMap = list()

    def createCollisionMap(self):
        for tile in self.level:
            if tile.hitBox == True:
                self.collisionMap.append(tile)

    def createLevel(self):
        self.level = list()
        for rowIndex,row in enumerate(self.LevelData):
            for colIndex,cell in enumerate(row):
                if not cell == " " or cell == 'o':
                    self.level.append(self.tileManager.createTile(cell, colIndex * tilsize , rowIndex * tilsize))

    def drawLevel(self,surface):
        for tile in self.level:
            pygame.draw.rect(surface,tile.color,tile.rect )
        
    def updateCollisions(self):
        for tile in self.level:
            if tile.color == 'red':
                break
            tile.rect.x += self.shift.x

    def scrool(self,player):
            keys = pygame.key.get_pressed()
            direction = player.direction.x
            center = player.rect.centerx
            if center < 500 and direction < 0 and keys[pygame.K_a]:
                self.shift.x = 3
                player.speed = 0
            elif center > 1000 and direction > 0 and keys[pygame.K_d]:
                self.shift.x = -3
                player.speed = 0
            else:
                self.shift.x = 0
                player.speed = 3

    def update(self,player):
        self.scrool(player)
        self.updateCollisions()
