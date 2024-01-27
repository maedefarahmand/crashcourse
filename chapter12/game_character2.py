import sys
import pygame
from settings2 import Settings
from character2 import Character
class alieninvasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("alien invasion")
        self.character=Character(self)

    def run_game(self):
        while True:

            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            
    def _update_screen(self):
        """update images in the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()

        pygame.display.flip()

        
if __name__=='__main__':
    ai=alieninvasion()
    ai.run_game()