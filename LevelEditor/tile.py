import pygame

class Tile:
    def __init__(self,left,top,color) -> None:
        self.heigth = 1
        self.width = 1
        self.rectangle = pygame.rect.Rect(left,top,self.width,self.heigth)
        self.color = color

    def draw(self,display):
            pygame.draw.rect(display,self.color,self.rectangle)
            