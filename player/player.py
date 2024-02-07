import pygame

class Player:
    def __init__(self, spawn, speed):
        self.spawn = spawn
        self.sprite = pygame.image.load('./assets/player.png').convert()
        self.direction = pygame.Vector2(0,0)
        self.rect = pygame.rect.Rect(spawn.x,spawn.y,79,75)
        self.color = pygame.Vector3(250,120,60)
        self.hasJump = True
        self.jumpSpeed = -15
        self.speed = speed
        self.friction = 0.2
        self.gravity = 0.8
        self.maxSpeed = 8
        self.minSpeed = 5
        self.alive = True
        self.isSuperPowerAllowed = True
        self.isMoveAllowed = True

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
        if keys[pygame.K_LSHIFT]:
            self.isSprinting = True
        else: self.isSprinting = False


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
        self.checkForDeath()
        self.checkSprint()

    def move(self):
        self.rect.x += self.direction.x * self.speed * self.isMoveAllowed

    def checkSprint(self):
        if self.isSprinting and self.speed <= self.maxSpeed:
            self.speed += 1
        elif not self.isSprinting and self.speed >= self.minSpeed:
            self.speed -= 1

    def checkForDeath(self):
        if self.rect.y > 900:
            self.alive = False
            self.isSuperPowerAllowed = True

    def draw(self,screen):
        isLookingLeft = False
        if self.direction.x > 0:
            isLookingLeft = False
        elif self.direction.x < 0:
            isLookingLeft = True

        screen.blit(pygame.transform.flip(self.sprite,isLookingLeft,False),(self.rect.x,self.rect.y + 8))
