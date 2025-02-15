import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,SHOT_RADIUS)

        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        
    def draw(self, screen):
        return pygame.draw.circle(screen, (255,255,255), self.position, self.radius,LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt