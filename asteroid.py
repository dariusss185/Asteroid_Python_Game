from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS,ASTEROID_MAX_RADIUS
from logger import log_event
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self,surface):
        pygame.draw.circle(surface,"crimson",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        angle=random.uniform(20,50)
        vector_a = self.velocity.rotate(angle)
        vector_b = self.velocity.rotate(-angle)
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)  # "built" with position + radius
        new_asteroid_2 = Asteroid(self.position.x,self.position.y, new_radius)  # "built" with position + radius
        new_asteroid_1.velocity = vector_a * 1.2
        new_asteroid_2.velocity = vector_b * 1.2 # "driving speed" set afterward
        

