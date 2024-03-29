import pygame

class CollisionHandler():
    def __init__(self,player,levelManager) -> None:
        self.player = player
        self.collisionMap = levelManager.collisionMap
        self.levelManager = levelManager
        self.killTiles = list()

    def update(self,player,collisionMap,dt):
        self.player = player
        self.collisionMap = collisionMap
        self.horizontalMovementCollisions(dt)
        self.verticalMovementCollisions(dt)
        
    def createKillTileList(self):
        self.killTiles = list()
        for tile in self.collisionMap:
            if 'Acid' in tile.imagePath:
                self.killTiles.append(tile.char)
                
    def checkForKillTiles(self,char):
        for ch in self.killTiles:
            if ch == char:
                self.player.die(self.levelManager)

    def horizontalMovementCollisions(self,dt):
        self.player.applyFriction()
        self.player.move(dt)         
        player_points = [self.player.rect.bottomleft, self.player.rect.bottomright]
        for tile in self.collisionMap:
            if any(tile.rect.collidepoint(point) for point in player_points):
                self.checkForKillTiles(tile.char)
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.x < 0:
                    self.player.rect.left = tile.rect.right
                elif self.player.direction.x > 0:
                    self.player.rect.right = tile.rect.left
                if tile.char == 'e':
                    self.playerJumpTile()
                if tile.char == 'f':
                    self.levelManager.loadNextLevel()
                    self.player.die(self.levelManager)
    
    def verticalMovementCollisions(self,dt):
        self.player.applyGravity(dt)
        for tile in self.collisionMap:
            if tile.rect.colliderect(self.player.rect):
                if self.player.direction.y > 0:
                    self.player.direction.y = 0
                    self.player.rect.bottom = tile.rect.top
                    self.player.hasJump = True
                elif self.player.direction.y < 0:
                    self.player.rect.top = tile.rect.bottom
                    self.player.direction.y = 0
                if tile.char == 'e':
                    self.playerJumpTile()
                
    def playerJumpTile(self):
        self.player.jumpHigh()





