# from tkinter import *
# def read_file():
#     filename = ent.get()
#     with open(filename) as f:
#         line = f.read()
#
#         big_text.insert('1.0',line)
#
# def save_file():
#     filename = ent.get()
#     with open(filename,'w') as f:
#         line = f.write(big_text.get(1.0,END))
#
# # основная программа
# window = Tk()
# window.title('Приложение на tkinter')
# window.geometry('500x200')
# window.iconbitmap(default='energy.ico')
#
# ent = Entry(width=30)
# ent.grid(column=1,row=0)
# but_open = Button(text='Открыть',width=15,command=read_file)
# but_save = Button(text='Сохранить',width=15,command=save_file)
# big_text = Text(width=60)
#
# but_open.grid(column=2,row=0)
# but_save.grid(column=3,row=0)
# big_text.grid(columnspan=4,rowspan=30)
#
# scroll = Scrollbar(orient="vertical",command=big_text.yview)
# scroll.grid(column=7,row=0,sticky=NS)
# big_text.config(yscrollcommand=scroll.set)
#
# window.mainloop()
# ********************************************************************************8

# from tkinter import *
# window = Tk()
# window.title('Приложение на tkinter')
# window.geometry('350x200')
# window.iconbitmap(default='energy.ico')
#
# class New_Radio():
#     def __init__(self,text):
#         self.lab = Label(width=20, height=30)
#         self.lab.pack(side=RIGHT)
#         self.fr = Frame()
#         self.var = IntVar()
#         self.var.set(0)
#         self.fr.pack(side=LEFT)
#         self.names = { 'Вася':'+79172223344',
#                        'Петя': '+79172473123',
#                        'Маша': '+79172993274'
#         }
#         i=0
#         for name in self.names:
#             aa = Radiobutton(self.fr,width=10,height=3,text =name,variable=self.var,
#                   value=i,indicatoron=0,command=self.click_radio)
#             i +=1
#             aa.pack()
#
#     def click_radio(self):
#         if self.var.get() == 0:
#             self.lab['text'] = '+79172223344'
#         elif self.var.get() == 1:
#             self.lab['text'] = '+79172473069'
#         elif self.var.get() == 2:
#             self.lab['text'] = '+79172663574'
#
# rad = New_Radio(window)
#
# window.mainloop()
# ****************************************************************************
# from tkinter import *
# window = Tk()
# window.title('Приложение на tkinter')
# window.geometry('350x200')
# window.iconbitmap(default='energy.ico')
#
# def add_item():
#     indicator = tovari_box.curselection()
#     a = tovari_box.get(indicator)
#     pokupki_box.insert(END,a)
#
# def del_list():
#     select =list(pokupki_box.curselection())
#     select.reverse()
#     for i in select:
#         pokupki_box.delete(i)
#
# tovari_box = Listbox(selectmode=EXTENDED)
# tovari_box.pack(side=LEFT)
# tovari = ['пирог','конфеты','молоко','гречка','чай','макароны','хлеб']
# for tovar in tovari:
#     tovari_box.insert(0,tovar)
# pokupki_box = Listbox(selectmode=EXTENDED)
# pokupki_box.pack(side=RIGHT)
#
# scroll = Scrollbar(command=tovari_box.yview())
# scroll.pack(side=LEFT,fill=Y)
# tovari_box.config(yscrollcommand=scroll.set)
#
# f = Frame()
# f.pack(side=LEFT,padx=10)
# add_but = Button(f, text='Добавить',command=add_item)
# add_but.pack(fill=X)
# del_but = Button(f, text='Удалить',command=del_list)
# del_but.pack(fill=X)
#
# window.mainloop()
# *******************************************************************
# from tkinter import *
#
# def change_enter(event):
#     a = ent.get()
#     list_box.insert(END,a)
#     ent.delete(0,END)
# def delet_box(event):
#     select = list(list_box.curselection())
#     select.reverse()
#     for i in select:
#         list_box.delete(i)
#
# def double_lab(event):
#     indicator = list_box.curselection()
#     a = list_box.get(indicator)
#     lab_text['text']= a
#
#
# window = Tk()
# window.title('Приложение на tkinter')
# window.geometry('350x250')
# window.iconbitmap(default='energy.ico')
#
# ent = Entry(width=70,bg='lightblue')
# ent.pack()
#
# list_box = Listbox(selectmode=EXTENDED)
# list_box.pack(side=LEFT)
# ent.bind('<Return>',change_enter)
# b = Button(text='Очистить список', width=15, height=3)
# b.bind('<Button-1>',delet_box)
# b.pack(side=LEFT)
#
# lab_text = Label(text='I am here',width=50)
# lab_text.pack(side=BOTTOM)
# list_box.bind('<Double-Button-1>',double_lab)
# window.mainloop()
# **********************************************************************
# from tkinter import *
# window = Tk()
# window.title('Приложение на tkinter')
# window.geometry('250x250')
# window.iconbitmap(default='energy.ico')
#
# def razm_text(event):
#     w = ent_weight.get()
#     h = ent_heigt.get()
#     text_opis['width']=w
#     text_opis['height']=h
# def color_text(event):
#     text_opis['bg']='grey'
# def color_text_green(event):
#     text_opis['bg']='green'
#
#
# ent_weight = Entry(width=5)
# ent_heigt = Entry(width=5)
# ent_heigt.place(x=50,y=10)
# ent_weight.place(x=50,y=30)
#
# ent_weight.bind('<Return>',razm_text)
# ent_heigt.bind('<Return>',razm_text)
# but_izm = Button(text='Изменить')
# but_izm.place(x=90,y=20)
# but_izm.bind('<Button-1>',razm_text)
#
# text_opis = Text(width=40,height=50)
# text_opis.place(x=5,y=65)
#
# text_opis.bind('<FocusIn>',color_text)
# text_opis.bind('<FocusOut>',color_text_green)
# text_opis.bind()
#
# window.mainloop()
#*********************************************
# from tkinter import *
# root = Tk()
#
# c = Canvas(root,width=800,height=800,bg='white')
# c.pack()
# c.create_oval(150,10,170,30,fill='yellow',outline='blue')
#
# c.create_rectangle(60,80,140,160,fill='yellow',width=3,outline='red',
#                    activefill='green', activedash=(15,1))
# c.create_polygon(50,80,150,80,100,40,fill='yellow',width=3,outline='red')
# j=3
# for i in range(60):
#     c.create_line(5+i*j,190,5+i*j,140,fill='green')
# # n=150
# for i in range(1,500,150):
#     c.create_oval(150+i, 10, 170+i, 30, fill='yellow', outline='blue')
#
# root.mainloop()
#**************************************************************
# from tkinter import *
# root = Tk()
# c= Canvas(root,width=200,height=200,bg='white')
# c.focus_set()
# c.pack()
# ball = c.create_oval(140,140,160,160,fill='green')
# c.bind('<Up>',lambda event:c.move(ball,0,-2))
# c.bind('<Down>',lambda event:c.move(ball,0,2))
# c.bind('<Left>',lambda event:c.move(ball,-2,0))
# c.bind('<Right>',lambda event:c.move(ball,2,0))





# root.mainloop()


# from tkinter import *
#
# root = Tk()
# c = Canvas(width=200, height=200,
#            bg='white')
# c.pack()
#
# rect = c.create_rectangle(
#     80, 80, 120, 120, fill='lightgreen')
#
#
# def in_focus(event):
#     c.itemconfig(rect, fill='green', width=2)
#     c.coords(rect, 70, 70, 130, 130)
#
#
# c.bind('<FocusIn>', in_focus)
#
# root.mainloop()

from tkinter import *


# def color(event):
#     c.itemconfig('group1', width=3,
#                  fill="red")
#
#
# root = Tk()
# c = Canvas(width=460, height=150,
#            bg='white')
# c.pack()
# oval = c.create_oval(30, 10, 130, 80,
#                      tag="group1")
# c.create_line(10, 100, 450, 100,
#               tag="group1")
# c.bind('<Button-3>', color)
# root.mainloop()
# **********************************************************8
# from tkinter import *
#
# def oval_func(event):
#     c.delete(oval)
#     c.create_text(80, 50,
#                   text="Круг")
#
#
# def rect_func(event):
#     c.delete("rect")
#     c.create_text(230, 50,
#                   text="Прямоугольник")
#
#
# def triangle(event):
#     c.delete(trian)
#     c.create_text(380, 50,
#                   text="Треугольник")
#
#
# c = Canvas(width=460, height=100,
#            bg='grey80')
# c.pack()
#
# oval = c.create_oval(30, 10, 130, 80,
#                      fill="orange")
# c.create_rectangle(180, 10, 280, 80,
#                    tag="rect",
#                    fill="lightgreen")
# trian = c.create_polygon(
#     330, 80, 380, 10, 430, 80,
#     fill='white', outline="black")
#
# c.tag_bind(oval, '<Button-1>', oval_func)
# c.tag_bind("rect", '<Button-1>', rect_func)
# c.tag_bind(trian, '<Button-1>', triangle)
#
# mainloop()
# *****************************************************************
# from tkinter import *
# def motion(event):
#     x = event.x
#     y = event.y
#     c.move(ball, x, y)
#     c.after(2000, motion)
#
# root = Tk()
# c = Canvas(root, width=500, height=500,bg="white")
# c.pack()
# ball = c.create_oval(0, 0, 40, 40,fill='green')
# root.bind('<Button-1>',motion)
#
# root.mainloop()
from tkinter import *
# *****************************************************
#
# from tkinter import *
# import random
# root = Tk()
# root.geometry('400x150')
# def ran_letter():
#     global am
#     am=random.choice(list(letters.keys()))
#     labRan['text']=am
#
# def ok_no(event):
#     slovo = ent.get()
#     ur = letters[am]
#     if slovo == ur:
#         Label(text='ok').grid(column=3, row=9)
#         v=lab_ok.cget('text')+1
#         lab_ok['text']=v
#     else:
#         Label(text='no').grid(column=3, row=9)
#
#     ent.delete(0,END)
#
# letters={'собака':'dog',
#          'кошка':'cat',
#          'машина':'car',
#          'зеленый':'freen',
#          'яблоко':'apple',
#          'серый':'grey',
#          'мяч':'ball'}
#
# labRan2 = Label(text='Случайное слово:')
# labRan2.grid(column=1,row=0)
#
# labRan = Label()
# labRan.grid(column=3,row=0)
#
# # Label(text='Ok/No').grid(column=3,row=9)
#
# labC = Label(text='Enter translate')
# labC.grid(column=1,row=3)
# ent = Entry()
# ent.grid(column=3,row=3)
# but1 = Button(width=30,text='Случайное слово',command=ran_letter)
# but1.grid(column=1,row=6)
#
# Label(text='Число угаданных слов: ').grid(column=1,row=7)
# lab_ok = Label(text=0)
# lab_ok.grid(column=4,row=7)
# ent.bind('<Return>',ok_no)
#
# root.mainloop()
#*********************************************************************
# ДОДЕЛАТЬ!
from tkinter import *
root = Tk()
root.geometry('400x200')
def save():
    t = ent_text.get(1.0,END)
    indicator = tip_save_box.curselection()
    a = tip_save_box.get(indicator)
    # filename = a
    with open(a,'w') as f:
        f.write(t)

ent_text=Text()
ent_text.grid(columnspan=5,row=3)
ent_text.focus()

but_Save= Button(width=30,text='Save',command=save)
but_Save.grid(column=1,row=0)

tip_save_box = Listbox(width=5,height=3,selectmode=EXTENDED)
tip_save_box.grid(column=1,row=2)
tip_save = ['.txt','.html']
for tip in tip_save:
    tip_save_box.insert(0,tip)
#
#
root.mainloop()
# ************************************************************************8
# ПРОГРАММА ДЛЯ ВЫЧИСЛЕНИЯ ИНДЕКСА МАССЫ ТЕЛА
# from tkinter import *
# root = Tk()
# root.geometry('300x100')
# def raschet():
#     v=ent_ves.get()
#     r=ent_rost.get()
#     if not v.isnumeric() or not r.isnumeric():
#         lab_t['text'] = 'Ошибка!'
#     imt=int(v)/(int(r)/100)**2
#     imt_f="{0:.2f}".format(imt)
#     if imt<16:
#         lab_t['text']=imt_f+' Выраженный дефицит'
#     elif 16<imt<18.5:
#         lab_t['text'] = imt_f + ' Недостаток'
#     elif 18.5<=imt<25:
#         lab_t['text'] = imt_f + ' Норма'
#     elif 25<=imt<=30:
#         lab_t['text'] = imt_f + ' Избыточная масса тела'
#     elif 30<imt <=35:
#         lab_t['text'] = imt_f + ' Ожирение'
#     # lab_t.delete(0, END)
#
# Label(text='Вес,кг').grid(column=1,row=1,sticky=W)
# ent_ves=Entry(width=15)
# ent_ves.grid(column=2,row=1)
#
# Label(text='Рост,см').grid(column=1,row=2,sticky=W)
# ent_rost=Entry(width=15)
# ent_rost.grid(column=2,row=2)
#
# Label(text='ИМТ').grid(column=1,row=3,sticky=W)
# but_raschet = Button(text='Рассчитать',command=raschet)
# but_raschet.grid(column=2,row=6)
#
# lab_t=Label(text='ok')
# lab_t.grid(column=2, row=3)
#
# root.mainloop()
# *********************************************************************
# from tkinter import *
# root = Tk()
# root.geometry('350x300')
# def save():
#     s = ent1.get()
#     Label(text=s).grid(column=1,row=10)
#
# def ListboxSelect():
#     select=box.curselection()
#     n=select[0]



# answer=['Фамилия','Имя','Отчество','Возраст','Адрес','Телефон']
# i=0
# b=[]
# for n in answer:
#     b.append(Label(text=n,width=15).grid(column=1,row=i,sticky=E))
#     i+=1
# j=0
# for n in range(len(answer)):
#     ent1 = Entry(width=15).grid(column=3,row=j,sticky=W)
#     j+=1
#
# but_save= Button(text='Save',command=save)
# but_save.grid(column=4,row=10)
#
# box=Listbox()
# box.grid(column=5,row=0)
# for n in range(len(answer)):
#     box.insert(n,answer[n])
# box.bind('<ListboxSelect>',ListboxSelect)
#
# root.mainloop()



