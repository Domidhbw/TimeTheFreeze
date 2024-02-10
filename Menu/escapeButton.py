import pygame

class EscapeButton():
    def __init__(self,filepath,x,y) -> None:
        self.rect = pygame.rect.Rect(x,y,100,40)
        self.sprite = pygame.transform.scale(pygame.image.load(filepath).convert(), (100, 50))


