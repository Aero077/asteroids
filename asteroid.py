import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        # Update the asteroid's position based on its speed and direction
        self.position += self.velocity * dt

    def __str__(self):
        return f"Asteroid {self.name}: Size {self.size}, Speed {self.speed}"

    def collide(self, other):
        if isinstance(other, Asteroid):
            return f"{self.name} collides with {other.name}"
        else:
            return f"{self.name} cannot collide with {other}"

    def split(self):
        self.kill()
        # Split the asteroid into smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
        return [new_asteroid1, new_asteroid2]


class Shot(CircleShape):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (int(self.position.x), int(self.position.y)), self.radius, width=0)

    def update(self, dt):
        # Update the shot's position based on its speed and direction
        self.position += self.velocity * dt

