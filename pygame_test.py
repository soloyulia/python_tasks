import pygame,os


widht =600
heigt = 400
FPS =30
red = (255,0,0)
green = (0,255,0)
white =(255,255,255)
# настройка папки ассетов
game_folder = os.path.dirname(__file__)
img_folder =os.path.join(game_folder,'images')
player_img =pygame.image.load(os.path.join(img_folder,'sprite1.png'))
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        # игнорируем белый цвет,заполн фон спрайта
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.center =(widht/2,heigt/2)
    def update(self):
        self.rect.x +=5
        if self.rect.left >widht:
            self.rect.right =0
        # self.rect.y +=5
        # if self.rect.bottom>heigt:
        #     self.rect.top = 0

# создаем игровое окно и игру
pygame.init()
screen = pygame.display.set_mode((widht,heigt))
pygame.display.set_caption('My first PyGame!')
clock = pygame.time.Clock()
# создание группы спрайтов
all_sprites = pygame.sprite.Group()
# добавим объект спрайт в группу спрайтов
player = Player()
all_sprites.add(player)
player2 =Player()
all_sprites.add(player2)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    # обновление
    all_sprites.update()

    # рендеринг
    screen.fill(red)
    all_sprites.draw(screen)
    # после всех отрисовок
    pygame.display.flip()

pygame.quit()