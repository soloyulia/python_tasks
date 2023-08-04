import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion():
    """класс для управления ресурсом и поведением игры"""
    def __init__(self):
        pygame.init()
        self.settings =Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_widht,
                                               self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship =Ship(screen)

        # self.bg.color =(230,230,230)
        # self.screen.fill('green')
    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            # self.screen.fill('green')
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
    #                 переместить корабль вправо
                    self.ship.rect.x +=1

    def _update_screen(self):
        """обновляет изображение на экране"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai =AlienInvasion()
    ai.run_game()

