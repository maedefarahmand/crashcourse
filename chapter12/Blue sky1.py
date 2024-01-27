import sys
import pygame
from settings import Settings
class Bluesky:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("blue sky")

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

        pygame.display.flip()

        
if __name__=='__main__':
    ai=Bluesky()
    ai.run_game()