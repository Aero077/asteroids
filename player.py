import pygame
from constants import *
from circleshape import CircleShape
from asteroid import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backward
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # shoot
            if self.timer <= 0:
                shot = self.shoot()
                shot.update(dt)
                self.timer = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        position = self.position + forward * self.radius
        shot = Shot(position.x, position.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot


