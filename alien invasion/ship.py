import pygame
class Ship():
    """класс для управления кораблем"""
    def __init__(self,ai_game):
        """инициализирует корабль и задает начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # загружает изображение корабля
        self.image = pygame.image.load('images/korabl_1.bmp')
        self.rect = self.image.get_rect()
        # каждый корабль появл у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
