import pygame

class EscapeMenu():
    def __init__(self) -> None:
        self.resumeButton = pygame.rect.Rect(100,300,100,40)
        self.restartButton = pygame.rect.Rect(300,300,100,40)
        self.quitToMainButton = pygame.rect.Rect(100,600,100,40)
        self.quitToDesktopButton = pygame.rect.Rect(300,600,100,40)
        self.allRects = [self.resumeButton,self.restartButton,self.quitToMainButton,self.quitToDesktopButton]
        

    def handleInput(self,mousePos,player,levelManager):
        mousePos = self.adjustMousePosition(mousePos)
        if self.resumeButton.collidepoint(mousePos):
            return 'playing'
        elif self.restartButton.collidepoint(mousePos):
            player.die(levelManager)
            return 'playing'
        elif self.quitToMainButton.collidepoint(mousePos):
            return 'levelSelection'
        elif self.quitToDesktopButton.collidepoint(mousePos):
            return 'quit'
        else:
            return'escape'

    def drawEscapeMenu(self,screen,window):
        screen.fill("darkgrey")
        for rect in self.allRects:
            pygame.draw.rect(screen,'red',rect)
        scaled_surface = pygame.transform.scale(screen, (pygame.display.Info().current_w, pygame.display.Info().current_h))
        window.blit(scaled_surface,(0,0))

    def adjustMousePosition(self,mousePos):
        scaleX = 1800 / pygame.display.Info().current_w
        scaleY = 900 / pygame.display.Info().current_h
        adjustedX = mousePos[0] * scaleX
        adjustedY = mousePos[1] * scaleY
        return int(adjustedX), int(adjustedY)