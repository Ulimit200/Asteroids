import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_rate = pygame.time.Clock()
    dt = 0

    #Group creation
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #change objects to auto add to their required groups
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #Create Player
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Create AsteroidField
    field = AsteroidField()
       
    #Main game loop
    while True:
        for event in pygame.event.get():
            #End game if the window is closed
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        #Update updateable items
        updatable.update(dt)
        for roids in asteroids:
            if roids.collision_check(ship) == True:
                print ("Game over!")
                return
            for bullets in shots:
                if roids.collision_check(bullets) == True:
                    roids.split()
                    bullets.kill()
        #Draw all drawable objects
        for drawing in drawable:
            drawing.draw(screen)
        #Refresh Screen
        pygame.display.flip()
        #Force game to run at FRAME_RATE
        frame_rate.tick(FRAME_RATE)
        #Get time passed between frames
        dt = frame_rate.get_time()/1000
        


if __name__ == "__main__":
    main()
