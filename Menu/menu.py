import pygame

class Menu:
    def __init__(self) -> None:
        self.selectedLevel = 0
        self.isLevelSelected = False
        self.levelOne = pygame.rect.Rect(100,200,100,20)

    def main(self,running,screen):
        while not self.isLevelSelected:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.isLevelSelected = self.handleMouse(pygame.mouse.get_pos())
            self.drawMenu(screen)


    def handleMouse(self,mousePos):
        if self.levelOne.collidepoint(mousePos):
            print('now load level one')
            return True
        
    def drawMenu(self,screen):
        screen.fill("darkgrey")
        pygame.draw.rect(screen,'red',self.levelOne)
        pygame.display.flip()
        
    
            
