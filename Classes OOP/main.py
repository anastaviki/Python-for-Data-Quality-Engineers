from tkinter import *
from tkinter.ttk import Combobox

class WindowMain( ):
    def __init__(self, p_title, p_lable):
        self.title = p_title
        self.window = Tk()
        self.window.geometry('400x250')
        self.lbl = Label(self.window, text=p_lable)

class Window (WindowMain):

    def __init__(self, p_title,p_lable =""  ):
        WindowMain.__init__(self, p_title,p_lable )
        self.combo = Combobox(self.window)
        self.btn = Button(self.window, text="Add", command=self.clicked)
        self.input_type = 0

    def show_window(self):

        self.window.title(self.title)
        self.lbl.grid(column=0, row=0)
        self.combo['values'] = ("News", "Privat ad", "Recipe")
        self.combo.current(0)  # установите вариант по умолчанию
        self.combo.grid(column=1, row=0)
        self.btn.grid(column=2, row=0)
        self.window.mainloop()
    def clicked(self):
        x = self.combo.get()
        self.input_type = x
        self.window.destroy()


window = Window("Add News", "Select Type of New")
window.show_window()
print (window.input_type)
window = Window("Add News")
window.show_window()
print (window.input_type)










