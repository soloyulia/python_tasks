import pygame
pygame.init()


W = 600
H = 400
r = 50
x = 300
y = 200
black = (0,0,0)
white = (255,255,255)
green = (0, 255,0)
red = (255,0,0)
blue = (0,0,255)
my_rect =pygame.Rect(200,200,200,100)
treugoln = [(150,200),(300,50),(450,200)]

screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Игровое окно")
screen.fill(green)

# mySurface = pygame.Surface((100,100))
# mySurface.fill((0,0,255))
# pygame.draw.rect(screen,black,(100,100,50,50),0)
# screen.blit(mySurface,(50,50))

pygame.display.flip()
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # рисуем круг и эллипс
    # pygame.draw.circle(screen,blue,(x,y),r)
    # pygame.draw.rect(screen, black, (my_rect), 3)
    # pygame.draw.circle(screen, red, (x, y), 20)
    # pygame.draw.ellipse(screen,blue,(200,300,100,50),2)

    # выводим текст
    # font = pygame.font.SysFont('couriernew',40)
    # text = font.render(str('hello'),True,red)
    # screen.blit(text, (70,70))

    # рисуем треугольник
    # pygame.draw.polygon(screen,red,(treugoln),3)

    # нарисовать дом с треуг.крышей и квадрт основанием
    pygame.draw.rect(screen,blue,my_rect)
    pygame.draw.polygon(screen,red,treugoln)



    # pygame.draw.circle(screen,red,(x,y),100)

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

