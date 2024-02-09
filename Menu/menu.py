import pygame

class Menu:
    def __init__(self) -> None:
        self.selectedLevel = 0
        self.isLevelSelected = False
        self.levelOne = pygame.rect.Rect(100,200,100,50)
        self.levelTwo = pygame.rect.Rect(300,200,100,50)

    def main(self,screen):
        while not self.isLevelSelected:
            for event in pygame.event.get():   
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handleMouse(pygame.mouse.get_pos())
                self.drawMenu(screen)


    def handleMouse(self,mousePos):
        if self.levelOne.collidepoint(mousePos):
            self.selectedLevel = 1
            self.isLevelSelected = True
        elif self.levelTwo.collidepoint(mousePos):
            self.selectedLevel = 2
            self.isLevelSelected = True
        
    def drawMenu(self,screen):
        screen.fill("darkgrey")
        pygame.draw.rect(screen,'red',self.levelOne)
        pygame.draw.rect(screen,'grey',self.levelTwo)
        pygame.display.flip()
        
    
            
