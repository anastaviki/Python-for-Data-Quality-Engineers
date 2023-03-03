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
# import all modules
import random
from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar
from datetime import datetime
from tkinter import filedialog as fd
import sys
import os
import re
sys.path.append(os.getcwd() + r"\Strings Object Func")  # add path
import string_pack as sp  # import string HW


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
    def __init__(self, p_title, p_lable=""):  # also have combobox, and button for exit from application
        WindowMain.__init__(self, p_title, p_lable)
        self.combo = Combobox(self.window)
        self.input_type = 0
        self.btn_ex = Button(self.window, text="Exit", command=self.exit_v)
        self.exit_code = 0

    def show_window(self):  # graw main window
        self.combo['values'] = ("News", "Privat ad", "Recipe", "Provide records with file")
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
        self.cal = Calendar(self.window, selectmode='day', year=2023, month=2, day=26)
        self.new_date = ""

    def show_window(self):  # draw window with adding aa add
        self.lbl_c.grid(column=0, row=3, sticky=NW)
        self.cal.grid(column=2, row=3, sticky=NW)
        WindowAddPub.show_window(self)

    def clicked(self):  # proceed with adding an add
        self.new_date = self.cal.get_date()
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


class ParcerFile:  # class for parsing file
    def __init__(self, p_file):
        self.path = p_file
        self.statr_rec = 0
        self.type_rec = ""
        self.text_of_rec = ""

    def parc(self):
        with open(self.path, 'r') as file:
            for line in file.readlines():
                if re.findall(r"^(\w|\s)+-+$", line):  # find first line of record
                    self.type_rec = line.replace('-', '').strip()
                    self.statr_rec = 1
                elif self.statr_rec == 1 and self.statr_rec == 1 and not re.match(r'^-+$', line):  # body of record
                    self.text_of_rec = self.text_of_rec + line
                elif self.statr_rec == 1:  # end of record
                    self.statr_rec = 0
                    if self.type_rec == "News":  # parsing of news body
                        parc_new = ParserNew(self.type_rec, self.text_of_rec)
                        parc_new.parc_rec()
                    elif self.type_rec == "Privat ad":  # parsing of add body
                        parc_add = ParserAdd(self.type_rec, self.text_of_rec)
                        parc_add.parc_rec()
                    else:  # parsing of recipe record
                        parc_rec = ParserRec(self.type_rec, self.text_of_rec)
                        parc_rec.parc_rec()

                    self.text_of_rec = ""


class ParserRecord:  # class for parsing body of record from file
    def __init__(self, p_type_rec, p_text):
        self.type_rec = p_type_rec
        self.text_of_record = p_text
        self.main_text = ""

    def parc_rec(self):
        pass


class ParserNew (ParserRecord):  # parsing of New body from file
    def __init__(self, p_type_rec, p_text):
        ParserRecord.__init__(self, p_type_rec, p_text)
        self.city = ""

    def parc_rec(self):
        self.city = self.text_of_record.split('\n')[0]

        self.main_text = sp.text_capitalise('\n'.join(self.text_of_record.split('\n')[1:]))
        new_from_file = News(self.type_rec, self.main_text, self.city)  # create a New object
        new_from_file.add_to_feed()


class ParserAdd (ParserRecord):  # parsing of Add body from file
    def __init__(self, p_type_rec, p_text):
        ParserRecord.__init__(self, p_type_rec, p_text)
        self.date = ""

    def parc_rec(self):
        self.date = self.text_of_record.split('\n')[0]
        self.main_text = sp.text_capitalise('\n'.join(self.text_of_record.split('\n')[1:]))
        add_from_file = Ads(self.type_rec, self.main_text, self.date)  # create an Add object
        add_from_file.add_to_feed()


class ParserRec (ParserRecord):  # parsing of Recipe body from file
    def __init__(self, p_type_rec, p_text):
        ParserRecord.__init__(self, p_type_rec, p_text)

    def parc_rec(self):
        self.main_text = sp.text_capitalise(self.text_of_record)
        rec_from_file = Rec(self.type_rec, self.main_text)   # create an Rec object
        rec_from_file.add_to_feed()


class Publication:  # class for publications
    def __init__(self, p_type, p_text):  # will have type and text
        self.type = p_type
        self.text = p_text
        self.first_row = ""
        self.now = datetime.now()

    @staticmethod
    def add_line_to_feed(line):  # add line to file
        with open('newsfeed.txt', 'a') as file:
            file.write(line.strip()+'\n')

    def add_first_row(self):  # add first row in publication
        self.first_row = self.type + '-'*(30-len(self.type))
        self.add_line_to_feed(self.first_row)

    def add_main_part(self):  # add main part of publication will have differences in child classes
        pass

    def add_last_row(self):  # add last row
        self.add_line_to_feed('-'*30)

    def add_to_feed(self):  # add publication to feed
        self.add_first_row()
        self.add_line_to_feed(self.text)
        self.add_main_part()
        self.add_last_row()
        self.add_line_to_feed("\n")
        self.add_line_to_feed("\n")


class News (Publication):  # class for news
    def __init__(self, p_type, p_text, p_city):  # also have city
        Publication.__init__(self, p_type, p_text)
        self.city = p_city

    def add_main_part(self):  # add main part of news
        self.add_line_to_feed(self.city + ", " + self.now.strftime("%d-%m-%Y %H:%M"))


class Ads (Publication):  # class for adds
    def __init__(self, p_type, p_text, p_date_until):  # also have expiration date and number of left days
        Publication.__init__(self, p_type, p_text)
        self.date_until = p_date_until
        self.days_left = 0

    def add_main_part(self):  # add main part of add
        self.days_left = str((datetime.strptime(self.date_until, '%m/%d/%y')-self.now).days)
        self.add_line_to_feed("Actual until: "+self.date_until+", " + self.days_left + " days left")


class Rec (Publication):  # class for recipes
    def __init__(self, p_type, p_text):  # also will have numbers of calories
        Publication.__init__(self, p_type, p_text)
        self.cal = random.randint(100, 1000)

    def add_main_part(self):  # add main part of recipes
        self.add_line_to_feed("Number of calories: " + str(self.cal))


window = Window("Add Publications", "Select Type of Publication")
window.show_window()  # add window for select type of publication
type_of_pub = window.input_type
# open window with adding new publications until exit from the app
while window.exit_code == 0:
    # depends on type of publication create an object of sutable class and proced adding publication to feed
    if type_of_pub == "News":
        add_new = WindowAddNews("Add New", "Fill all fields", "Add text of the new:")
        add_new.show_window()
        new = News(type_of_pub, add_new.new_text, add_new.city)
        new.add_to_feed()

    elif type_of_pub == "Privat ad":
        add_ad = WindowAddAd("Add New", "Fill all fields", "Add text of the ad:")
        add_ad.show_window()
        ad = Ads(type_of_pub, add_ad.new_text, add_ad.new_date)
        ad.add_to_feed()

    elif type_of_pub == "Recipe":
        add_rec = WindowAddRec("Add New", "Fill all fields", "Add new Receipe:")
        add_rec.show_window()
        rec = Rec(type_of_pub, add_rec.new_text)
        rec.add_to_feed()
    else:
        add_file = WindowAddFromFile("Add New", "Select file")
        add_file.show_window()
        par = ParcerFile(add_file.filename)
        par.parc()
    window = Window("Add Publications", "Select Type of Publication")
    window.show_window()
    type_of_pub = window.input_type
