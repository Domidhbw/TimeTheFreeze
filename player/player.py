import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x,self.y,30,30)
        self.color = pygame.Vector3(250,120,60)
        self.velX = 0
        self.velY = 0
        self.maxVel = 300
        self.downforce = 400
        self.hasJump = True
        self.right_pressed = False
        self.left_pressed = False
        self.jump_pressed = False
        self.jumpSpeed = 1200
        self.applyGravity = True
        self.speed = speed
        self.friction = 10
        self.leftHit = False
        self.rightHit = False
        self.downHit = False
        self.groundCheck = pygame.Rect(self.x+2,(self.y+30),20,1)
        self.upperCheck = pygame.Rect(self.x,(self.y-30),30,1)
        self.rightCheck = pygame.Rect((self.x+30),self.y,5,30)
        self.leftCheck = pygame.Rect((self.x-30),self.y,5,30)

    
    def update(self,dt):
        if self.downHit:
            self.applyGravity = False
            self.hasJump = True 
            self.downHit = False
        else:
            self.applyGravity = True

        if self.left_pressed:
            self.velX += self.speed 
        if self.right_pressed:
            self.velX -= self.speed 
        if self.jump_pressed and self.hasJump:
            self.hasJump = False
            self.y -= self.jumpSpeed * dt
            self.applyGravity = True

        if self.velX > 0:
            self.velX -= self.friction
        else:
            self.velX += self.friction 

        if self.velX > self.maxVel:
            self.velX = self.maxVel
        if  self.velX < -self.maxVel:
            self.velX = -self.maxVel

        if self.leftHit:
            self.velX = 5
            self.leftHit = False
        if self.rightHit:
            self.velX = -5
            self.rightHit = False

        self.x += self.velX * dt

        if self.applyGravity:
            self.y += self.downforce * dt

        self.rect = pygame.Rect(int(self.x),int(self.y),30,30)
        self.updateCheck()
        print(self.velX)


    def updateCheck(self):
        self.groundCheck = pygame.Rect(int(self.x+1),int(self.y+33),15,1)
        self.rightCheck = pygame.Rect(int(self.x+30),int(self.y),1,25)
        self.leftCheck = pygame.Rect(int(self.x),int(self.y),1,25)
        self.upperCheck = pygame.Rect(int(self.x),int(self.y),30,1)

