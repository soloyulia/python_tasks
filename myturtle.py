import turtle, time, random
t = turtle.Pen()
window = turtle.Screen()
# t.speed(2)
# length =10
# count = 0
# while count < 20:
#     t.forward(length)
#     t.left(60)
#     length=length+10
#     count+=1
#******************
# t.speed(4)
# t.up()
# t.goto(-30,40)
# t.fillcolor('red')
# t.begin_fill()
# t.goto(-30,70)
# t.goto(-80,70)
# t.goto(-80,40)
# t.goto(-30,40)
# t.end_fill()
# t.speed(2)
# t.up()
# t.goto(50,30)
# t.down()
# t.fillcolor('red')
# t.begin_fill()
#
# t.circle(40)
# t.end_fill()
# *****************************************************************
# рисуем квадрат
# def kvadrat(a):
#     for i in range(0,4):
#         t.color(colors[i % 4])
#         t.forward(a)
#         t.left(90)
#
# t.speed(100)
# colors = ['red','blue','green','orange']
# dl = 6
# for i in range(40):
#     t.color(colors[i%4])
#     t.circle(dl)
#     # t.right(10)
#     dl +=4
# t.fillcolor('red')

# МНОГОУГОЛЬНИК .n - количество сторон
# def mnogoygolnik(n, dlina):
#     sum_angle = (n-2)*180
#     if sum_angle % n == 0:
#         angle = sum_angle//n
#         for i in range(n):
#             t.forward(100)
#             t.left(180-angle)
#
# # mnogoygolnik(80,kol_storon)
# for i in range(3,10):
#     mnogoygolnik(i,50)
#
# РИСУЕМ ЗВЕЗДУ*************************************
# n - количество вершин
# рисуем желтые звезды на черном небе
# def star_fill(n,dlina):
#     t.begin_fill()
#     if n % 2 != 0:
#         for i in range(n):
#             t.forward(dlina)
#             angle = n // 2 * 360 / n
#             t.left(angle)
#     t.end_fill()
#
# window.bgcolor('black')
# t.color('yellow')
# t.speed(0)
# for i in range(15):
#     x = random.randint(-320,320)
#     y = random.randint(-220,220)
#     t.up()
#     t.setposition(x,y)
#     t.down()
#     size = random.randint(10,20)
#     versina = random.choice([5,7,9,11,13,15])
#     star_fill(versina,size)
#
# time.sleep(5)
# **************************************************
# ПРЫГАЮЩИЙ МЯЧИК

# отрисовка границы
# t.speed(0)
# t.up()
# t.hideturtle()
# t.pensize(5)
# t.color('red')
# t.goto(300,300)
# t.down()
# t.goto(300,-300)
# t.goto(-300,-300)
# t.goto(-300,300)
# t.goto(300,300)
#
# # рисуем шарик ball
# ball = turtle.Pen()
# ball.hideturtle()
# ball.shape('circle')
# ball.up()
# randx =random.randint(-290,290)
# randy =random.randint(-290,290)
#
# ball.goto(randx,randy)
# ball.showturtle()
# dx = 3
# dy = 4
# while True:
#         x,y = ball.position()
#         if x+dx >=300 or x+dx<=-300:
#             dx = -dx
#         if y + dy >= 300 or y + dy <= -300:
#             dy = -dy
#         ball.goto(x+dx,y+dy)



# **************************************************
# ПРЫГАЮЩИЙ МЯЧИК

# отрисовка границы
t.speed(0)
t.up()
t.hideturtle()
t.pensize(5)
t.color('red')
t.goto(300,300)
t.down()
t.goto(300,-300)
t.goto(-300,-300)
t.goto(-300,300)
t.goto(300,300)

# рисуем шарик ball
balls = []
coutn = 5
for i in range(coutn):
    ball = turtle.Pen()
    ball.hideturtle()
    ball.shape('circle')
    ball.up()
    randx =random.randint(-290,290)
    randy =random.randint(-290,290)
    ball.goto(randx,randy)
    ball.showturtle()
    dx = random.randint(-5,5)
    dy = random.randint(-5,5)
    balls.append([ball,dx,dy])

for i in balls:
    print(i)
while True:
    for i in range(coutn):
        balls[i]
        x,y = ball.position()
        if x+dx >=300 or x+dx<=-300:
            dx = -dx
        if y + dy >= 300 or y + dy <= -300:
            dy = -dy
        ball.goto(x+dx,y+dy)





window.mainloop()