import pygame

class slider():
    def __init__(self) -> None:
        self.pos = pygame.Vector2(650,700)
        self.length = 500
        self.height = 5
        self.handleSize = pygame.Vector2(20,40)
        self.handlePos = pygame.Vector2(self.pos.x + self.length,self.pos.y - (self.handleSize.y // 2))
        self.dragging = False

    def update(self,mousePos):
        mousePos = self.adjustMousePosition(mousePos)

        if mousePos[0] >= self.pos.x and mousePos[0] <= (self.pos.x + self.length):
            self.handlePos.x = mousePos[0]

        volume = self.handlePos.x - 600
        volume = float(volume)
        volume = volume / 510

        return volume

    def drawSlide(self, screen):
        pygame.draw.rect(screen, 'red', (self.pos.x, self.pos.y, self.length, self.handleSize.y))
        pygame.draw.rect(screen, 'blue', (self.handlePos.x, self.handlePos.y, self.handleSize.x, self.handleSize.y))

    def adjustMousePosition(self,mousePos):
        scaleX = 1800 / pygame.display.Info().current_w
        scaleY = 900 / pygame.display.Info().current_h
        adjustedX = mousePos[0] * scaleX
        adjustedY = mousePos[1] * scaleY
        return int(adjustedX), int(adjustedY)
