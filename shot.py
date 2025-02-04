import pygame
from constants import *
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        print("Before super call")  # Add this debug print
        super().__init__(x, y, 5)
        print("After super call")   # Add this debug print
        print("shots created")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt