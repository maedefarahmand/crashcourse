import pygame
class Character:
    """a class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image=pygame.image.load('chapter12/images/istockphoto-1438381490-612x612.jpg')
        self.rect=self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)