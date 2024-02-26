import pygame
import json
from .levelButton import LevelButton
from .escapeButton import EscapeButton

class Menu:
    def __init__(self) -> None:
        self.saveFilePath = './saveFile.json'
        self.endButton = EscapeButton('./assets/Buttons/End.png',800,600)
        self.levelStatus = self.loadLevelStatus()
        self.possibleLevels = []
        self.selectableLevels = self.getLevels(True)
        self.unselectableLevels = self.getLevels(False)
        self.levels = self.createLevelList()
        self.background = pygame.image.load('./assets/Background.png').convert()
  
    def menuStart(self):
        self.levelStatus = self.loadLevelStatus()
        self.possibleLevels = []
        self.selectableLevels = self.getLevels(True)
        self.unselectableLevels = self.getLevels(False)
        self.levels = self.createLevelList()

    def handleMouse(self,mousePos,levelManager,player):
        mousePos = self.adjustMousePosition(mousePos)
        for levelButon in self.levels:
            if levelButon.rect.collidepoint(mousePos) and levelButon.isAllowed:
                levelManager.loadNewLevel(levelButon.number)
                player.die(levelManager)
                return 'playing'
        if self.endButton.rect.collidepoint(mousePos):
            return 'quit'
        return 'levelSelection'

    def draw(self,screen,window):
        self.menuStart()
        screen.blit(self.background,(0,0)) 
        for levelButton in self.levels:
            screen.blit(levelButton.sprite,(levelButton.rect.x,levelButton.rect.y))
        screen.blit(self.endButton.sprite,(self.endButton.rect.x,self.endButton.rect.y))
        scaled_surface = pygame.transform.scale(screen, (pygame.display.Info().current_w, pygame.display.Info().current_h))
        window.blit(scaled_surface,(0,0))

    def adjustMousePosition(self,mousePos):
        scaleX = 1800 / pygame.display.Info().current_w
        scaleY = 900 / pygame.display.Info().current_h
        adjustedX = mousePos[0] * scaleX
        adjustedY = mousePos[1] * scaleY
        return int(adjustedX), int(adjustedY)
        
    def loadLevelStatus(self):
        try:
            with open(self.saveFilePath, 'r') as file:
                data = json.load(file)
                return data['levels']
        except FileNotFoundError:
            return {}
        
    def getLevels(self,getSelectables):
        if getSelectables:
            selectableLevels = []
            for level,completed in self.levelStatus.items():
                self.possibleLevels.append(level)
                if completed == True:
                    selectableLevels.append(level)
            return selectableLevels
        else:
            unSelectableLevels = []
            for level,completed in self.levelStatus.items():
                if completed == False:
                    unSelectableLevels.append(level)
            return unSelectableLevels

    def createLevelList(self):
        origin = pygame.Vector2(350,300)
        levelButtonList = list()
        for level in self.possibleLevels:
            if level in self.selectableLevels:
                levelButtonList.append(LevelButton(str(level),origin.x,origin.y,True))   
            else:
                levelButtonList.append(LevelButton(str(level),origin.x,origin.y,False))
            origin.x += 200
        return levelButtonList
        

