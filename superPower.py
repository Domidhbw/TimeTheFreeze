import pygame
from Level.tileManager import TileManager

class doSuperPower:
    def __init__(self,collisionMap,level) -> None:
        self.collisionMap = collisionMap
        self.level = level
        self.isAllowed = True
        self.tileM = TileManager()
    
    def doIt(self,player):
        if self.isAllowed:
            tile = self.tileM.createClone(player)
            player.rect.x = player.spawn.x
            player.rect.y = player.spawn.y
            self.level.append(tile)
            self.collisionMap.append(tile)
            self.isAllowed = False
  