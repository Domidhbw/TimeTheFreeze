import pygame

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed


