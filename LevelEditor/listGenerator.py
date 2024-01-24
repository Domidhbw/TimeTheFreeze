import pygame
from tile import Tile

class LevelGenerator:
    def __init__(self,filepath,screen) -> None:
        self.file = open(filepath,"r").read()
        self.Width = self.getLevelSize()
        self.Height = self.getLevelHeight()
        self.tileScale = self.getScale(screen)
        self.level = self.createLevel()

    def getLevel(self):
        return self.level
    
    def getScale(self,screen:pygame.display):
        width,height = screen.get_size()
        nHorizontalTiles =  width / self.Width
        nVerticalTiles = height / self.Height
        return nHorizontalTiles,nVerticalTiles

    def createLevel(self):
        origin = pygame.Vector2(0,0)
        level = list()
        for char in self.file:
            match char:
                case "x":
                    level.append(Tile(origin.x,origin.y,"Blue"))
                    origin.x += self.tileScale[1]
                case "o":
                    level.append(Tile(origin.x,origin.y,"Black"))
                    origin.x += self.tileScale[1]
                case "i":
                    level.append(Tile(origin.x,origin.y,"Green"))
                    origin.x += self.tileScale[1]
                case ",":
                    origin.x = 0
                    origin.y += self.tileScale[0]
        return level
    
    def getLevelSize(self):
        count = -1
        for char in self.file:
            if char != " ":
                count += 1
                if char == ",":
                    break
        return count
    def getLevelHeight(self):
        height = 0
        for char in self.file:
            if char == ",": 
                height += 1
        return height
