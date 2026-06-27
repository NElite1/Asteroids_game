import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self,x,y,):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0

        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(1, 0).rotate(self.rotation) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)

    def rotate(self, amount: float):
        self.rotation += amount

    def move(self, distance: float):
        self.position += pygame.Vector2(0, -1).rotate(self.rotation) * distance

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)

        if keys[pygame.K_w]:
            self.move(PLAYER_SPEED * dt)

        if keys[pygame.K_s]:
            self.move(-PLAYER_SPEED * dt)
    

        