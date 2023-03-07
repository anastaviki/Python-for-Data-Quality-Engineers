from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar
from tkinter import filedialog as fd
from datetime import datetime
# create class for gui
class WindowMain:
    def __init__(self, p_title, p_lable):  # class will have title, lable, button and window itself
        self.title = p_title
        self.window = Tk()
        self.lbl = Label(self.window, text=p_lable)
        self.btn = Button(self.window, text="Add", command=self.clicked)

    def show_window(self):  # def for draw gui
        self.lbl.grid(column=0, row=0, sticky=NW)
        self.window.geometry('800x800')
        self.window.title(self.title)
        self.window.mainloop()

    def clicked(self):  # def for click button, will change in children classes
        pass


class Window (WindowMain):  # main window for select type of publication
    def __init__(self, p_title, p_lable="", p_lable_color=0):  # also have combobox, and button for exit from application
        WindowMain.__init__(self, p_title, p_lable)
        self.combo = Combobox(self.window)
        self.input_type = 0
        self.btn_ex = Button(self.window, text="Exit", command=self.exit_v)
        self.exit_code = 0
        self.lable_color = p_lable_color

    def show_window(self): # graw main window
        if self.lable_color == 1:
            self.lbl.config(bg="Red")
        self.combo['values'] = ("News", "Privat ad", "Recipe", "Provide records with file",
                                "Provide New with file", "Provide Private ad with file",
                                "Provide Recipe with file")
        self.combo.current(0)
        self.combo.grid(column=1, row=0)
        self.btn.grid(column=2, row=0)
        self.btn_ex.grid(column=3, row=0)
        WindowMain.show_window(self)

    def exit_v(self):  # for exit from application
        self.exit_code = 1
        self.window.destroy()

    def clicked(self):  # select publication type
        x = self.combo.get()
        self.input_type = x
        self.window.destroy()


class WindowAddPub (WindowMain):  # class for adding publications
    def __init__(self, p_title, p_lable, p_lable_2):  # also will have some input and one more lable
        WindowMain.__init__(self, p_title, p_lable)
        self.lbl_n = Label(self.window, text=p_lable_2)
        self.text_n = Text(self.window, width=80, height=5, bg="#C0C0C0", fg='black', wrap=WORD)
        self.new_text = ""

    def show_window(self):  # draw window for add publication
        self.lbl_n.grid(column=0, row=2, sticky=NW)
        self.text_n.grid(column=2, row=2)
        self.btn.grid(column=1, row=4)
        WindowMain.show_window(self)

    def clicked(self):  # for proceed with adding new record
        self.new_text = self.text_n.get("1.0", "end-1c")
        self.window.destroy()


class WindowAddNews(WindowAddPub):  # class for adding news
    def __init__(self, p_title, p_lable, p_lable_2):  # also have city input and one more lable
        WindowAddPub.__init__(self, p_title, p_lable, p_lable_2)
        self.lbl_c = Label(self.window, text="City:")
        self.text_c = Text(self.window, width=80, height=1, bg="#C0C0C0", fg='black')
        self.city = ""

    def show_window(self):  # draw window with adding a new
        self.lbl_c.grid(column=0, row=3, sticky=NW,  ipady=6,  pady=4)
        self.text_c.grid(column=2, row=3,  ipady=6,  pady=4)
        WindowAddPub.show_window(self)

    def clicked(self):  # proceed with adding a new
        self.city = self.text_c.get("1.0", "end-1c")
        WindowAddPub.clicked(self)


class WindowAddAd(WindowAddPub):  # class for adds
    def __init__(self, p_title, p_lable, p_lable_2):  # also will have expiration date
        WindowAddPub.__init__(self, p_title, p_lable, p_lable_2)
        self.lbl_c = Label(self.window, text="Expired day:")
        self.cal = Calendar(self.window, selectmode='day',
                            year=datetime.now().year,
                            month=datetime.now().month,
                            day=datetime.now().day)  # current date here
        self.new_date = ""

    def show_window(self):  # draw window with adding aa add
        self.lbl_c.grid(column=0, row=3, sticky=NW)
        self.cal.grid(column=2, row=3, sticky=NW)
        WindowAddPub.show_window(self)

    def validation(self):  # add function for check date
        current_date = datetime.now()
        if datetime.strptime(self.new_date, '%m/%d/%y') < current_date:
            self.lbl_c.config(text="Please select a future date.")
            self.lbl_c.config(bg="Red")
            return 0
        else:
            return 1

    def clicked(self):  # proceed with adding an add
        self.new_date = self.cal.get_date()
        if self.validation() == 1:  # if validation ok - close the window
            WindowAddPub.clicked(self)


class WindowAddRec(WindowAddPub):  # class for recipes
    def __init__(self, p_title, p_lable, p_lable_2):  # will have only one input
        WindowAddPub.__init__(self, p_title, p_lable, p_lable_2)


class WindowAddFromFile(WindowMain):  # class for adding from file
    def __init__(self, p_title, p_lable):  # will have only one input
        WindowMain.__init__(self, p_title, p_lable)
        self.btn_file = Button(self.window, text="Select", command=self.select_file)
        self.btn_def = Button(self.window, text="Default file", command=self.def_file)
        self.filename = "input.txt"

    def show_window(self):  # draw window with adding aa add
        self.btn_file.grid(column=2, row=0)
        self.btn_def.grid(column=3, row=0)
        WindowMain.show_window(self)

    def select_file(self):  # select file
        self.filename = fd.askopenfilename()
        self.window.destroy()

    def def_file(self):  # for default file
        self.window.destroy()


class WindowAddNewFromFile (WindowAddFromFile):
    def __init__(self, p_title, p_lable):
        WindowAddFromFile.__init__(self, p_title, p_lable)


class WindowAddAddFromFile (WindowAddFromFile):
    def __init__(self, p_title, p_lable):
        WindowAddFromFile.__init__(self, p_title, p_lable)


class WindowRecipeFromFile (WindowAddFromFile):
    def __init__(self, p_title, p_lable):
        WindowAddFromFile.__init__(self, p_title, p_lable)