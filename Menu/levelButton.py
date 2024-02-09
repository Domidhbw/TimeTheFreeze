import pygame

class LevelButton():
    def __init__(self,num,x,y,isAllowed) -> None:
        self.number = num
        self.rect = pygame.rect.Rect(x,y,100,40)
        self.isAllowed = isAllowed
        self.color = 'red'
        if self.isAllowed:
            self.color = 'red'
        else:
            self.color = 'grey'
