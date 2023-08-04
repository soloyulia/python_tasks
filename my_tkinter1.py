from tkinter import *

class Block():
    def __init__(self,master):
        self.colors = {
            '#ff0000':'красный',
            '#ff7d00':'оранжевый',
            '#ffff00':'желтый',
            '#00ff00':'зеленый',
            '#007dff':'голубой',
            '#0000ff':'синий',
            '#7d00ff':'фиолетовый'
        }
        self.lab = Label(master, width=50,height=2,background='white')
        self.ent = Entry(master,width=20,justify=CENTER)

        self.lab.pack()
        self.ent.pack()
        for color in self.colors:
            aa = Button(master,width=20,background=color)
            aa.bind('<Button-1>', self.red_click)
            aa.pack()


    def red_click(self, q):
        self.clear()
        color = q.widget.cget('bg');
        self.ent.insert(0, color)
        self.lab['text'] =self.colors[color]
    def clear(self):
        self.ent.delete(0, END)

# основная программа
window = Tk()
window.title('Приложение на tkinter')
window.geometry('500x300')
window.iconbitmap(default='energy.ico')
first_block = Block(window)


window.mainloop()