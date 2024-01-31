import pygame
from LevelEditor.tile import Tile

class doSuperPower:
    def __init__(self,collisionMap,level) -> None:
        self.collisionMap = collisionMap
        self.level = level
        self.isAllowed = True
    
    def doIt(self,player):
        if self.isAllowed:
            tile = Tile(player.rect.x,player.rect.y,30,60,'red')
            player.rect.x = player.spawn.x
            player.rect.y = player.spawn.y
            self.level.append(tile)
            self.collisionMap.append(tile)
            self.isAllowed = False
  