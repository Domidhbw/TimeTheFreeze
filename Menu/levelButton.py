import pygame

class LevelButton():
    def __init__(self,num,x,y,isAllowed) -> None:
        self.number = num
        self.rect = pygame.rect.Rect(x,y,100,40)
        self.isAllowed = isAllowed
        self.sprite = self.loadSprite()
        if not self.isAllowed:
            self.sprite = pygame.transform.scale(pygame.image.load('./assets/Buttons/Level0.png').convert(), (100, 50))

    def loadSprite(self):
        path = './assets/Buttons/Level' + str(self.number) + '.png'
        return pygame.transform.scale(pygame.image.load(path).convert(), (100, 50))
