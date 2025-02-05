import pygame
from circleshape import CircleShape
import constants
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill()
        else: 
            self.kill()
            new_angle = random.uniform(20, 50)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            self.velocity *= 1.2
            asteroid1.velocity = self.velocity.rotate(new_angle)
            asteroid2.velocity = self.velocity.rotate(-new_angle) 
            
            #new_asteroid1 = Asteroid(self.x, self.y, new_radius)
            #new_asteroid2 = Asteroid(self.x, self.y, -new_radius)

        

