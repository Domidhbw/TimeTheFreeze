import pygame

class LevelButton():
    def __init__(self,num,x,y,isAllowed) -> None:
        self.number = num
        self.rect = pygame.rect.Rect(x,y,100,40)
        self.isAllowed = isAllowed
        self.sprite = self.loadSprite()
        if not self.isAllowed:
            self.sprite = './assets/Level0.png'

    def loadSprite(self):
        path = './assets/Buttons/Level' + str(self.number) + '.png'
        return pygame.image.load(path).convert()
