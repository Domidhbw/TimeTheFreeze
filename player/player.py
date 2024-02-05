import pygame

class Player:
    def __init__(self, spawn, speed):
        self.spawn = spawn
        self.direction = pygame.Vector2(0,0)
        self.rect = pygame.rect.Rect(spawn.x,spawn.y,30,60)
        self.color = pygame.Vector3(250,120,60)
        self.hasJump = True
        self.jumpSpeed = -20
        self.speed = speed
        self.friction = 0.1
        self.gravity = 0.8

    def getKeyPressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
        if keys[pygame.K_SPACE]:
            if self.hasJump:
                self.jump()
                self.hasJump = False

    def applyGravity(self):
        self.direction.y += self.gravity 
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jumpSpeed

    def applyFriction(self):
        if self.direction.x > 0.1:
            self.direction.x -= self.friction
        if self.direction.x < -0.1:
            self.direction.x += self.friction 

    def update(self):
        self.getKeyPressed()

    def move(self):
        self.rect.x += self.direction.x * self.speed
