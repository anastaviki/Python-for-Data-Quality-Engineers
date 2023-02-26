# Description
# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
#
# 2.Provide record type required data
#
# 3.Record is published on text file in special format
# You need to implement:
#
# 1.News – text and city as input. Date is calculated during publishing.
#
# 2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
#
# 3.Your unique one with unique publish rules.
#
# Each new record should be added to the end of file.Commit file in git for review.


from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar
import datetime


class WindowMain:
    def __init__(self, p_title, p_lable):
        self.title = p_title
        self.window = Tk()
        self.lbl = Label(self.window, text=p_lable)
        self.btn = Button(self.window, text="Add", command=self.clicked)

    def show_window(self):
        self.lbl.grid(column=0, row=0, sticky=NW)
        self.window.geometry('800x800')
        self.window.title(self.title)
        self.window.mainloop()


class Window (WindowMain):
    def __init__(self, p_title,p_lable =""  ):
        WindowMain.__init__(self, p_title,p_lable )
        self.combo = Combobox(self.window)
        self.input_type = 0

    def show_window(self):
        self.combo['values'] = ("News", "Privat ad", "Recipe")
        self.combo.current(0)  # установите вариант по умолчанию
        self.combo.grid(column=1, row=0)
        self.btn.grid(column=2, row=0)
        WindowMain.show_window(self)

    def clicked(self):
        x = self.combo.get()
        self.input_type = x
        self.window.destroy()


class WindowAddPub (WindowMain):
    def __init__(self, p_title, p_lable, p_lable_2):

        WindowMain.__init__(self, p_title,p_lable )
        self.lbl_n = Label(self.window, text=p_lable_2)
        self.text_n = Text(self.window,width=80, height=5, bg="#C0C0C0", fg='black', wrap=WORD)
        self.new_text = ""


    def show_window (self):
        self.lbl_n.grid(column=0, row=2,sticky=NW)
        self.text_n.grid(column=2, row=2)
        self.btn.grid(column=1, row=4)
        WindowMain.show_window(self)

    def clicked (self):
        self.new_text = self.text_n.get("1.0", "end-1c")
        self.window.destroy()


class WindowAddNews(WindowAddPub):
    def __init__(self, p_title, p_lable,p_lable_2):
        WindowAddPub.__init__(self, p_title,p_lable, p_lable_2)
        self.lbl_c = Label(self.window, text="City:")
        self.text_c = Text(self.window, width=80, height=1, bg="#C0C0C0", fg='black')
        self.city = ""

    def show_window (self):
        self.lbl_c.grid(column=0, row=3, sticky=NW,  ipady=6,  pady=4)
        self.text_c.grid(column=2, row=3,  ipady=6,  pady=4)
        WindowAddPub.show_window(self)

    def clicked(self):
        self.city = self.text_c.get("1.0", "end-1c")
        WindowAddPub.clicked(self)


class WindowAddAd(WindowAddPub):
    def __init__(self, p_title, p_lable, p_lable_2):
        WindowAddPub.__init__(self, p_title, p_lable, p_lable_2)
        self.lbl_c = Label(self.window, text="Expired day:")
        self.cal = Calendar(self.window, selectmode='day',year=2023, month=2,day=26)
        self.new_date = ""

    def show_window (self):
        self.lbl_c.grid(column=0, row=3,sticky=NW)
        self.cal.grid(column=2, row=3,sticky=NW)
        WindowAddPub.show_window(self)

    def clicked (self):
        self.new_date = self.cal.get_date()
        WindowAddPub.clicked(self)


class WindowAddRec(WindowAddPub):
    def __init__(self, p_title, p_lable, p_lable_2):
        WindowAddPub.__init__(self, p_title, p_lable, p_lable_2)


class Publication:
    def __init__(self, p_type, p_text):
        self.type = p_type
        self.text = p_text
        self.first_row =""
    def add_line_to_feed(self, line):
        with open('newsfeed.txt', 'a') as file:
            file.write(line.strip()+'\n')
    def add_first_row (self):
        self.first_row= self.type + '-'*(30-len(self.type))
        self.add_line_to_feed(self.first_row)
    def add_main_part(self):
        pass
    def add_last_row (self):
        self.add_line_to_feed('-'*30)
    def add_to_feed(self):
        self.add_first_row()
        self.add_line_to_feed(self.text)
        self.add_main_part()
        self.add_last_row()





class News (Publication):
    def __init__(self, p_type, p_text,p_city):
        Publication.__init__(self, p_type, p_text)
        self.city =p_city
        self.now = datetime.datetime.now()
    def add_main_part(self):
        self.add_line_to_feed(self.city +", "+self.now.strftime("%d-%m-%Y %H:%M"))






window = Window("Add Publications", "Select Type of Publication")
window.show_window()
type_of_pub= window.input_type
if type_of_pub == "News":
    add_new = WindowAddNews("Add New", "Fill all fields", "Add text of the new:")
    add_new.show_window()
    new = News(type_of_pub, add_new.new_text,add_new.city)
    new.add_to_feed()

elif type_of_pub == "Privat ad":
    add_ad = WindowAddAd("Add New", "Fill all fields", "Add text of the ad:")
    add_ad.show_window()
    print(add_ad.new_text)
    print(add_ad.new_date)
else:
    add_rec = WindowAddRec("Add New", "Fill all fields", "Add new Receipe:")
    add_rec.show_window()
    print(add_rec.new_text)





















