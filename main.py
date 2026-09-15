import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from logger import log_state
from player import Player
from asterofield import AsteroidField
from asteroid import Asteroid
from shot import Shot
from logger import log_event
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0.0
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Shot.containers=(shots,drawable,updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers=updatable
    asteroid_field = AsteroidField()
    
    user=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if user.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        screen.fill("Black")
        
        for drawing in drawable:
            drawing.draw(screen)
        
 
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:",SCREEN_HEIGHT)
    print("Hello from asteroids!")


if __name__ == "__main__":
    main()
