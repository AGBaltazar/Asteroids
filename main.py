import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def background():     
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    return screen

def background_overlay(screen, player):
        font = pygame.font.Font(None, 40)
        text = font.render(f"Health: {player.health} Enemies Dispersed: {player.dispersed_count}", True, "white")
        text_position = text.get_rect(centerx= SCREEN_WIDTH /2, y =10)
        overlay = pygame.draw.rect(screen, "white", rect= text_position, width= 1)
        screen.blit(text, text_position)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 #DeltaTime

    #Background Initilization
    screen = background()

    #Player initialization
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #Asteroid initialization
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    #Shooting initialization
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    while True:
        screen.fill("black")
        background_overlay(screen, player)
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        player.timer -= dt
        player.move(dt)
        pygame.display.flip()
        if player.invinsible == True:
            player.invinsible_timer -=dt
        if player.invinsible_timer<= 0:
            player.invinsible = False
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisions(asteroid):
                    player.dispersed_count +=1
                    asteroid.split()
        for i in asteroids:
            if i.collisions(player):
                if player.invinsible == False:
                    player.cooldown_overshield()
                if player.health == 0:
                    print("Game over!")
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()