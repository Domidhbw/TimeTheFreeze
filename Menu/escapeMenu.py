import pygame

from .escapeButton import EscapeButton
from .slideButton import slider

class EscapeMenu():


    def __init__(self,musicHandler) -> None:
        self.resumeButton = EscapeButton('./assets/Buttons/Resume.png',750,350)
        self.restartButton = EscapeButton('./assets/Buttons/Restart.png',950,350)
        self.quitButton = EscapeButton('./assets/Buttons/Menu.png',750,450)
        self.quitToDesktop = EscapeButton('./assets/Buttons/End.png',950,450)
        self.allSprites = [self.resumeButton,self.restartButton,self.quitButton,self.quitToDesktop]
        self.background = pygame.image.load('./assets/Background.png').convert()
        self.musicSlider = slider()
        self.musicHandler = musicHandler


    def handleInput(self,mousePos,player,levelManager):
        mousePos = self.adjustMousePosition(mousePos)
        if self.resumeButton.rect.collidepoint(mousePos):
            return 'playing'
        elif self.restartButton.rect.collidepoint(mousePos):
            player.die(levelManager)
            return 'playing'
        elif self.quitButton.rect.collidepoint(mousePos):
            return 'levelSelection'
        elif self.quitToDesktop.rect.collidepoint(mousePos):
            return 'quit'
        else:
            self.musicHandler.changeVolume(self.musicSlider.update(mousePos))
            return'escape'

    def drawEscapeMenu(self,screen,window):
        screen.blit(self.background,(0,0)) 
        for button in self.allSprites:
            screen.blit(button.sprite,(button.rect.x,button.rect.y)) 
        self.musicSlider.drawSlide(screen)
        scaled_surface = pygame.transform.scale(screen, (pygame.display.Info().current_w, pygame.display.Info().current_h))
        window.blit(scaled_surface,(0,0))

    def adjustMousePosition(self,mousePos):
        scaleX = 1800 / pygame.display.Info().current_w
        scaleY = 900 / pygame.display.Info().current_h
        adjustedX = mousePos[0] * scaleX
        adjustedY = mousePos[1] * scaleY
        return int(adjustedX), int(adjustedY)