import pygame

class Player:
    def __init__(self) -> None:
        self.player_pos = pygame.Vector2(50,50)
        self.rectangle = pygame.rect.Rect(self.player_pos.x,self.player_pos.y,30,30)
        self.downforce = 10
        self.hasJump = True
        self.groundCheck = self.rectangle

    def updateGroundCheck(self):
        self.groundCheck = self.rectangle.update(self.rectangle.left - 40,self.rectangle.top,self.rectangle.width,self.rectangle.height)