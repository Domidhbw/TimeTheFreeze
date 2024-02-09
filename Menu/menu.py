import pygame

class Menu:
    def __init__(self,windowWidth,windowHeight) -> None:
        self.selectedLevel = 0
        self.isLevelSelected = False
        self.reachedLevel = 1
        self.levelOne = pygame.rect.Rect(200,200,100,50)
        self.levelTwo = pygame.rect.Rect(300,200,100,50)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

    def main(self,screen,window):
        while not self.isLevelSelected:
            for event in pygame.event.get():   
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handleMouse(pygame.mouse.get_pos())
                self.drawMenu(screen,window)

    def handleMouse(self,mousePos):
        if self.levelOne.collidepoint(mousePos) and self.reachedLevel >0:
            self.selectedLevel = 1
            self.isLevelSelected = True
        elif self.levelTwo.collidepoint(mousePos) and self.reachedLevel >1:
            self.selectedLevel = 2
            self.isLevelSelected = True
        
    def drawMenu(self,screen,window):
        screen.fill("darkgrey")
        pygame.draw.rect(screen,'red',self.levelOne)
        pygame.draw.rect(screen,'grey',self.levelTwo)
        scaled_surface = pygame.transform.scale(screen, (self.windowWidth, self.windowHeight))
        window.blit(scaled_surface,(0,0))
        pygame.display.flip()
        

