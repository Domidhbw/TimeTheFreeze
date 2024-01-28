import pygame

class Tile:
    def __init__(self,left,top,color) -> None:
        self.heigth = 1
        self.width = 1
        self.rectangle = pygame.rect.Rect(left,top,self.width,self.heigth)
        self.color = color
        self.image = pygame.image.load("ground.png")

    def draw(self,display):
            if self.color == "Blue":
                 self.image = pygame.transform.scale(self.image,(self.rectangle.width,self.rectangle.height))
                 display.blit(self.image,self.rectangle)
            else:
                 pygame.draw.rect(display,self.color,self.rectangle)
            