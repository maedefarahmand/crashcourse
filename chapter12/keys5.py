import sys
import pygame
from settings5 import Settings
class rocket:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("keys")

    def run_game(self):
        while True:

            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """respond to key presses and mouse events"""
        for event in pygame.event.get():
            
            if event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
           
            
    def _check_keydown_events(self,event):
        """respond to keypresses"""    
        print(event.key)
        if event.key==pygame.K_q:
            sys.exit()

                    
    def _update_screen(self):
        """update images in the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

        
if __name__=='__main__':
    ai=rocket()
    ai.run_game()