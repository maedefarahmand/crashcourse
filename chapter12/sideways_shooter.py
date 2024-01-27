import sys
import pygame
from settings6 import Settings
from ship6 import Ship
from bullet6 import Bullet
class sideways_shooter:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("alien invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()


    def run_game(self):
        while True:

            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """respond to key presses and mouse events"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        """respond to keypresses"""    
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        """respond to key releases""" 
        if event.key==pygame.K_UP:
            self.ship.moving_up=False
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=False

    def _fire_bullet(self):
        """create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""

        #update bullet positions
        self.bullets.update()

        #get rid of bullets that have disappeared
       
        for bullet in self.bullets.copy():
            if bullet.rect.right>=self.settings.screen_width:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """update images in the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        pygame.display.flip()

        
if __name__=='__main__':
    ai=sideways_shooter()
    ai.run_game()