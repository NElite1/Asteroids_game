import pygame
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *



def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids=pygame.sprite.Group()

    Player.containers=(updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidfield=AsteroidField()
    while True:
        updatable.update(dt)
        log_state()
        screen.fill('black')
        dt = clock.tick(60) / 1000
        for player in drawable:
            player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        


if __name__ == "__main__":
    main()
