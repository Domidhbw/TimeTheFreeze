import pygame

class Player:
    def __init__(self, spawn, speed, musicHandler):
        self.spawn = spawn
        self.sprite = pygame.image.load('./assets/player.png').convert()
        self.direction = pygame.Vector2(0,0)
        self.rect = pygame.rect.Rect(spawn.x,spawn.y,79,69)
        self.color = pygame.Vector3(250,120,60)
        self.hasJump = True
        self.jumpSpeed = -900
        self.speed = speed
        self.friction = 0.2
        self.gravity = 48
        self.maxSpeed = 480
        self.minSpeed = speed
        self.alive = True
        self.isSuperPowerAllowed = True
        self.isMoveAllowed = True
        self.musicHandler = musicHandler

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

    def applyGravity(self,dt):
        self.direction.y += self.gravity 
        self.rect.y += self.direction.y *dt

    def jump(self):
        self.musicHandler.playSoundJump()
        self.direction.y = self.jumpSpeed

    def applyFriction(self):
        if self.direction.x > 0.1:
            self.direction.x -= self.friction
        if self.direction.x < -0.1:
            self.direction.x += self.friction

    def update(self,levelManager):
        self.getKeyPressed()
        self.checkForDeath(levelManager)
        self.checkSprint()

    def move(self,dt):
        self.rect.x += self.direction.x * self.speed * self.isMoveAllowed * dt

    def checkSprint(self):
        if self.isSprinting and self.speed <= self.maxSpeed:
            self.speed += 60
        elif not self.isSprinting and self.speed >= self.minSpeed:
            self.speed -= 60

    def die(self,levelManager):
        levelManager.resetLevel()
        self.musicHandler.playSoundDie()
        self.rect.x = self.spawn.x
        self.rect.y = self.spawn.y
        self.alive = True
        self.isSuperPowerAllowed = True
        self.direction = pygame.Vector2(0,0)
        pass

    def checkForDeath(self,levelManager):
        if self.rect.y > 900:
            self.die(levelManager)
            
    def draw(self,screen):
        isLookingLeft = False
        if self.direction.x > 0:
            isLookingLeft = False
        elif self.direction.x < 0:
            isLookingLeft = True

        screen.blit(pygame.transform.flip(self.sprite,isLookingLeft,False),(self.rect.x,self.rect.y + 8))

    def jumpHigh(self):
       self.direction.y = self.jumpSpeed *2  