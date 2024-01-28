import pygame

class Tile:
    def __init__(self,left,top,Width,Height,color) -> None:
        self.heigth = Height
        self.width = Width
        self.rect = pygame.rect.Rect(left,top,self.width,self.heigth)
        self.color = color
        self.image = pygame.image.load("ground.png")

    def draw(self,display):
            if self.color == "Blue":
                 self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
                 display.blit(self.image,self.rect)
            else:
                 pygame.draw.rect(display,self.color,self.rect)
            