import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.color = pygame.Vector3(250,120,60)
        self.velX = 0
        self.velY = 0
        self.maxVel = 8
        self.downforce = 5
        self.hasJump = True
        self.right_pressed = False
        self.left_pressed = False
        self.jump_pressed = False
        self.jumpSpeed = 110
        self.applyGravity = True
        self.speed = speed
        self.friction = 0.2
        self.groundCheck = pygame.Rect(self.x+2,(self.y+30),20,1)
        self.upperCheck = pygame.Rect(self.x,(self.y-30),30,1)
        self.rightCheck = pygame.Rect((self.x+30),self.y,1,30)
        self.leftCheck = pygame.Rect((self.x-30),self.y,1,30)

    
    def update(self,dt):
        if self.left_pressed:
            self.velX += self.speed * dt
        if self.right_pressed:
            self.velX -= self.speed * dt
        if self.jump_pressed and self.hasJump:
            self.hasJump = False
            self.y -= self.jumpSpeed
            self.applyGravity = True

        if self.velX > 0:
            self.velX -= self.friction
        else:
            self.velX += self.friction

        if self.velX > self.maxVel:
            self.velX = self.maxVel
        if  self.velX < -self.maxVel:
            self.velX = -self.maxVel

        self.x += self.velX

        if self.applyGravity:
            self.y += self.downforce

        self.rect = pygame.Rect(int(self.x),int(self.y),30,30)
        self.updateCheck()
        print(self.velX)


    def updateCheck(self):
        self.groundCheck = pygame.Rect(int(self.x+8),int(self.y+30),15,1)
        self.rightCheck = pygame.Rect(int(self.x+30),int(self.y),1,30)
        self.leftCheck = pygame.Rect(int(self.x),int(self.y),1,30)
        self.upperCheck = pygame.Rect(int(self.x),int(self.y),30,1)

