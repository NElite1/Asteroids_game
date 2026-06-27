import random
from circleshape import *
from constants import *
from logger import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = (self.velocity * dt) + self.position 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            a1_vel = self.velocity.rotate(angle)
            a2_vel = self.velocity.rotate(-1 * angle)
            self.radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position,self.position,self.radius)
            asteroid_2 = Asteroid(self.position,self.position,self.radius)
            asteroid_1.velocity = a1_vel * 2
            asteroid_2.velocity = a2_vel * 2

            
            
