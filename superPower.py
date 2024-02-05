import pygame
from Level.tileManager import TileManager

class doSuperPower:
    def __init__(self) -> None:
        self.tileM = TileManager()
    
    def doIt(self,player,levelManager):
        if player.isSuperPowerAllowed:
            player.isSuperPowerAllowed = False
            tile = self.tileM.createClone(player)
            tile.rect.update(tile.rect.left,tile.rect.top,player.rect.width,player.rect.height)
            player.rect.x = player.spawn.x
            player.rect.y = player.spawn.y
            a = levelManager.level[-1].rect.x
            levelManager.resetLevel()
            b = levelManager.level[-1].rect.x
            c = b-a
            tile.rect.x += c
            levelManager.level.append(tile)
            levelManager.collisionMap.append(tile)


  