import pygame,sys,math
from pygame.locals import *
pygame.init()
# блок инициализации
pygame.event.set_blocked([MOUSEBUTTONDOWN,KEYDOWN])
(window_wight,window_height,window_title) = (600,400,'Simple Figure')

screen = pygame.display.set_mode((window_wight,window_height),0,32)
pygame.display.set_caption(window_title)
rect1_color = (255,0,255)
rect2_color = (0,0,255)
rect1_rect = Rect((10,10),(100,100))
rect2_rect =Rect((150,150),(300,100))
rect1_wight =0
rect2_wight =4
arc_color = (0,0,0)
arc_rect = Rect((200,250),(300,100))
arc_start_angle =math.pi
arc_end_angle =math.pi*0.5

poligon_color = (255,0,0)
poligon_points =[(200,200),(300,300),(400,150)]
# helloText ='Hello,World!'
# (x,y,fontSize) = (10,40,40)
# myFont =pygame.font.SysFont =('None',fontSize)
fontColor = (255,0,0)
bgColor = (255,255,255)
circle_pos = (100,100)
circle_color = (255,0,0)
circle_radius = 50
ellipse_color=(0,255,0)
ellipse_rect = Rect((200,10),(350,150))
line_start_pos =(100,100)
line_end_pos = (300,300)
aaline_start_pos =(110,100)
aaline_end_pos =(310,300)
lines_color =(0,0,0)

# fontImage = myFont.render(helloText,0,(fontColor))

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
    pygame.draw.rect(screen,rect1_color,rect1_rect,rect1_wight)
    pygame.draw.rect(screen,rect2_color,rect2_rect,rect2_wight)
    pygame.draw.polygon(screen,poligon_color,poligon_points,0)
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
    pygame.draw.ellipse(screen,ellipse_color,ellipse_rect,0)
    pygame.draw.arc(screen,arc_color,arc_rect,arc_start_angle,arc_end_angle)
    pygame.draw.line(screen,lines_color,line_start_pos,line_end_pos)
    pygame.draw.aaline(screen,lines_color,aaline_start_pos,aaline_end_pos,0)

    pygame.display.update()
pygame.quit()