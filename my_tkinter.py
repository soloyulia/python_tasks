import random
from tkinter import *
from tkinter import ttk
import random
breadth = 500
highness = 400
color =['gray','black','red','blue','orange','yellow','green']


def buttonClick():
    for n in range(1,300):
        x = random.randint(0,breadth)
        y = random.randint(0,highness)
        z = random.randint(2,15)
        dye = color[random.randint(0,7)]
        graphic.create_oval(x,y,x+z,y+z,fill =dye)

        # font = random.randint(10,30)
        # graphic.create_text(random.randint(0,breadth),random.randint(0,breadth),
        #                     text ='hello',fill=dye,font=('arial',font))
        # graphic.create_rectangle(20,20,breadth-20,highness-20)
        # graphic.create_oval(20,20,breadth-20,highness-20)
        # graphic.create_line(breadth/2,20,breadth/2,highness-20,fill=dye)
        # graphic.create_line(20,highness/2,breadth-20,highness/2,fill=dye)
        # graphic.create_line(0,n*4,breadth,highness-n*4,fill=dye)
        # graphic.create_line(n*6,0,breadth-n*6,highness,fill=dye)
        # graphic.create_rectangle(n*10,n*10,breadth-n*10,highness-n*10,fill=dye)

def str_sort_list(event):
    s = ent.get()
    s = s.split()
    s.sort()
    lab['text'] = ''.join(s)
def mouseDraw():
    x = event.x -1
    y = event.y -1
    graphic.create_oval(x,y,x+3,y+3)

# основная программа
window = Tk()
window.title('Приложение на Tkinter. Графика')
window.iconbitmap(default='energy.ico')
window.geometry('500x500')
# window.config(width=500,height=330)
display = Label(text='Я изучаю tkinter')
display.pack()
button = Button(window,text='Посмотреть!',command=buttonClick)
button.place(x=breadth/2-60,y=highness/2-15,width=120,height=30)
button.pack()

ent = Entry(window,width=20)
but = Button(window,text='Преобразовать')
lab = Label(window,width=20,background='black',foreground='white')
but.bind('<Button-1>',str_sort_list)
ent.pack()
but.pack()
lab.pack()


graphic = Canvas(window,width=breadth,height=highness,background='black')
graphic.bind('<Button-1>',mouseDraw)
graphic.pack()



window.mainloop()