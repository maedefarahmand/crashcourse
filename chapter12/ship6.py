import pygame
class Ship:
    """a class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen=ai_game.screen
        self.settings=ai_game.settings

        self.screen_rect=ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image=pygame.image.load('chapter12/images copy/ship.bmp')
        self.rect=self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midleft=self.screen_rect.midleft

        #store a float for the ship's exact horizontal position
        self.y=float(self.rect.y)


        #movement flag: start with a ship that's not moving
        self.moving_up=False
        self.moving_down=False
    def update(self):
        """update the ship position based on movement flag"""
        #update the ship's x value, not the rect
        if self.moving_up and self.rect.height > 0:
            self.y-=self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y+=self.settings.ship_speed
        #update rect object from self.x
        self.rect.y=self.y
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
