import pygame
from .tile import Tile

class LevelGenerator:
    def __init__(self,filepath) -> None:
        self.file = open(filepath,"r").read()
        self.tileScale = (50,50)
        self.ground = list() 
        self.level = self.createLevel()
        self.shift = 0

    def getLevel(self):
        return self.level
    
    def createLevel(self):
        origin = pygame.Vector2(0,0)
        level = list()
        for char in self.file:
            match char:
                case "x":
                    level.append(Tile(origin.x,origin.y,self.tileScale[1],self.tileScale[0],"Blue"))
                    self.ground.append(Tile(origin.x,origin.y,self.tileScale[1],self.tileScale[0],"Blue"))
                    origin.x += self.tileScale[1]
                case "o":
                    origin.x += self.tileScale[1]
                case "i":
                    level.append(Tile(origin.x,origin.y,self.tileScale[1],self.tileScale[0],"Green"))
                    origin.x += self.tileScale[1]
                case ",":
                    origin.x = 0
                    origin.y += self.tileScale[0]
        return level
    
    def drawLevel(self,screen):
        for tile in self.level:
            tile.draw(screen)


    def updateCollisions(self):
        for tile in self.ground:
            tile.rect.x += self.shift
        for tile in self.level:
            if tile.color == 'red':
                break
            tile.rect.x += self.shift


    def scrool(self,player):
        keys = pygame.key.get_pressed()
        direction = player.direction.x
        center = player.rect.centerx
        if center < 500 and direction < 0 and keys[pygame.K_a]:
            self.shift = 5
            player.speed = 0
        elif center > 1000 and direction > 0 and keys[pygame.K_d]:
            self.shift = -5
            player.speed = 0
        else:
            self.shift = 0
            player.speed = 5
        
    def update(self,screen,player):
        self.updateCollisions()
        self.drawLevel(screen)
        self.scrool(player)
        

            

