import pygame
from constants import *
from player import *



def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frame_rate = pygame.time.Clock()
    dt = 0
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        ship.update(dt)
        ship.draw(screen)
        pygame.display.flip()
        frame_rate.tick(FRAME_RATE)
        dt = frame_rate.get_time()/1000
        


if __name__ == "__main__":
    main()
