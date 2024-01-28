import pygame
from LevelEditor.tile import Tile

class doSuperPower:
    def __init__(self,player,collisionMap,level) -> None:
        self.player = player
        self.collisionMap = collisionMap
        self.level = level
        self.tile = Tile(0,0,0,0,self.player.color)
    
    def doIt(self):
        self.tile.rect = self.player.rect
        self.collisionMap.append(self.tile)
        self.level.append(self.tile)
  