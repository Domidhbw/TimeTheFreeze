import pygame
from .tile import Tile
from .level import *

class TileManager:
    def __init__(self) -> None:
        self.tileInformation = tiles

    def createTile(self,char,left,top):
        if char in self.tileInformation.keys():
            match char:
<<<<<<< Updated upstream
                case 'x':
=======
                case 'f':
>>>>>>> Stashed changes
                    return Tile(left,top,self.tileInformation[char],char,True)
                case _:
                    return Tile(left,top,self.tileInformation[char],char,True)
        else:
            print('key does not exist check your colors and test level')
    
    def createClone(self,player):
        return Tile(player.rect.left,player.rect.top,'./assets/player.png','p',True)
        