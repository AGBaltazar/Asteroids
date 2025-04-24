import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 #DeltaTime
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for sprite in updatable:
            sprite.move(dt)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()