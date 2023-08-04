import pygame,sys,math,os
from pygame.locals import *
pygame.init()
# блок инициализации
pygame.event.set_blocked([MOUSEBUTTONDOWN,KEYDOWN])
(window_wight,window_height,window_title) = (600,400,'PyGame Image')

screen = pygame.display.set_mode((window_wight,window_height),0,32)
pygame.display.set_caption(window_title)
bgColor = (255,255,255)
image1 = pygame.image.load(os.path.join('images','image2.png'))
image2 = pygame.image.load(os.path.join('images','image3.png'))
newSurf = pygame.Surface((window_wight,window_height))
newSurf.blit(image1,(0,0))
newSurf.blit(image2,(100,100))
stringImage1 = pygame.image.tostring(image1,'RGB')
stringImage2 = pygame.image.tostring(image2,'RGBA')

newImage1 = pygame.image.fromstring(stringImage1,(128,128), 'RGBA')
newImage2 = pygame.image.fromstring(stringImage2,(128,128),'RGBA')
newSurf.blit(newImage1,(0,256))
newSurf.blit(newImage2,(128,256))
# pygame.image.save(newSurf,os.path.join('images','save_image2.png'))
# print('save image2.png')
# if pygame.image.get_extended():
#     print('My Pygame the best')
# else:
#     raise SystemExit


mainloop = True
while mainloop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainloop=False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                circle_pos=event.pos
        if event.type == KEYDOWN:
            mainloop=False


    screen.fill(bgColor)


    # screen.blit(fontImage,(x,y))
    # блок формирования кадра

    screen.blit(newSurf,(0,0))
    pygame.display.update()
pygame.quit()