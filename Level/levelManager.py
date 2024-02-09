import pygame
from .level import *
from .tileManager import TileManager

class LevelManager:
    def __init__(self,svManager) -> None:
        self.LevelData = level_map
        self.tileManager = TileManager()
        self.level = list()
        self.shift = pygame.Vector2()
        self.overallXShift = 0
        self.collisionMap = list()
        self.currentLevel = 1
        self.svManager = svManager

    def createCollisionMap(self):
        self.collisionMap = list()
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
            surface.blit(tile.sprite,(tile.rect.x,tile.rect.y))
        
    def updateCollisions(self):
        for tile in self.level:
            tile.rect.x += self.shift.x
            self.overallXShift += self.shift.x

    def scrool(self,player,dt):
            keys = pygame.key.get_pressed()
            direction = player.direction.x
            center = player.rect.centerx
            if center < 500 and direction < 0 and keys[pygame.K_a]:
                self.shift.x = player.speed *dt
                player.isMoveAllowed = False
            elif center > 1000 and direction > 0 and keys[pygame.K_d]:
                self.shift.x = -player.speed*dt
                player.isMoveAllowed = False
            else:
                self.shift.x = 0
                player.isMoveAllowed = True


    def loadNewLevel(self,level):
        self.currentLevel = level
        if level > self.svManager.levelVar:
            self.svManager.writeCurrentLevel(level)
        filePath = './Levels/level' + str(level) + '.txt'
        print(filePath)
        with open(filePath, 'r') as file:
            # Read lines without stripping
            level = [line.rstrip('\n') for line in file]
        self.LevelData = level

    def loadNextLevel(self):
        self.loadNewLevel(self.currentLevel + 1)

    def resetLevel(self):
        self.createLevel()
        self.createCollisionMap()

    def update(self,player,dt):
        self.scrool(player,dt)
        self.updateCollisions()
