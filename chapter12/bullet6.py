import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """create a bullet object at the ship's current position"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        #create a bullet rect at (0,0) and then set current position
        self.rect=pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft=ai_game.ship.rect.midleft
        # store the bullet position as a float

        self.x=float(self.rect.x)
    def update(self):
        """move the bullet up the screen"""
        #update the exact position of the bullet
        self.x+=self.settings.bullet_speed
        #update the rect position
        self.rect.x=self.x

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)