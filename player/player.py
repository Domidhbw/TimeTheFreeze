import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x,self.y,8,8)
        self.color(250,120,60)
        self.velX = 0
        self.velY = 0
        self.right_pressed = False
        self.left_pressed = False
        
        self.speed = 2

    
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        
        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x),int(self.y),8,8)

