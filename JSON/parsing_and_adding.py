import random
from datetime import datetime
import sys
import os
import re
import json
sys.path.append(os.getcwd() + r"\Strings Object Func")  # add path
import string_pack as sp  # import string HW


class ParcerFile:  # class for parsing file
    def __init__(self, p_file, p_record):
        self.path = p_file
        self.statr_rec = 0
        self.type_rec = ""
        self.text_of_rec = ""
        self.record = p_record
        self.type_verify = 0
        self.number_of_records = {'new': 0, 'add': 0, "recipe": 0}

    def verify_file(self):  # for file verification
        with open(self.path, 'r') as file:
            for line in file.readlines():
                if re.findall(r"^(\w|\s)+-+$", line):  # find first line of record
                    self.type_rec = line.replace('-', '').strip()
                    if self.type_rec == "News":
                        self.number_of_records["new"] = self.number_of_records["new"]+1
                    elif self.type_rec == "Privat ad":
                        self.number_of_records["add"] = self.number_of_records["add"]+1
                    else:
                        self.number_of_records["recipe"] = self.number_of_records["recipe"]+1
        if self.record == "New" and self.number_of_records["new"] == 1 and self.number_of_records["add"] == 0 and \
                self.number_of_records["recipe"] == 0:
            self.type_verify = 1
        elif self.record == "Add" and self.number_of_records["new"] == 0 and self.number_of_records["add"] == 1 and \
                self.number_of_records["recipe"] == 0:
            self.type_verify = 1
        elif self.record == "Recipe" and self.number_of_records["new"] == 0 and self.number_of_records["add"] == 0 and \
                self.number_of_records["recipe"] == 1:
            self.type_verify = 1
        elif self.record == "Records" and self.number_of_records["new"] + self.number_of_records["add"] + \
                self.number_of_records["recipe"] >= 2:
            self.type_verify = 1
        else:
            self.type_verify = 0

    def parc(self):
        self.verify_file()
        if self.type_verify == 1:  # ony if file verification - ok
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
            os.remove(self.path)


# class for parsing json files
class ParserJson(ParcerFile):
    def __init__(self, p_file, p_record):
        ParcerFile.__init__(self, p_file, p_record)
        self.data = ''
        self.error_in_date = 0
        self.rec = {}

    def verify_record(self, rec):  # verify each particular record
        try:
            if rec["type_of_record"] == "New":
                self.number_of_records["new"] += 1
            elif rec["type_of_record"] == "Add":
                self.number_of_records["add"] += 1
            elif rec["type_of_record"] == "Recipe":
                self.number_of_records["recipe"] += 1
            current_date = datetime.now()
            if rec["type_of_record"] == "Add" and datetime.strptime(rec["expiration_date"], '%m/%d/%y') > current_date:
                self.error_in_date = 0
            else:
                self.error_in_date = 1

        except KeyError:
            print('Check keys')

    def verify_file(self):  # verify file
        with open(self.path) as f:
            self.data = json.load(f)
            if "Records" in self.data:
                for rec in self.data["Records"]:
                    self.verify_record(rec)
            else:
                self.verify_record(self.data)

        if self.record == "New" and self.number_of_records["new"] == 1 and self.number_of_records["add"] == 0 and \
                self.number_of_records["recipe"] == 0:
            self.type_verify = 1
        elif self.record == "Add" and self.number_of_records["new"] == 0 and self.number_of_records["add"] == 1 and \
                self.number_of_records["recipe"] == 0 and self.error_in_date == 0:
            self.type_verify = 1
        elif self.record == "Recipe" and self.number_of_records["new"] == 0 and self.number_of_records["add"] == 0 and \
                self.number_of_records["recipe"] == 1:
            self.type_verify = 1
        elif self.record == "Records" and self.number_of_records["new"] + self.number_of_records["add"] + \
                self.number_of_records["recipe"] >= 2:
            self.type_verify = 1
        else:
            self.type_verify = 0

    def parse_record(self, p_rec):  # parse record and create record in file
        self.record = p_rec["type_of_record"]
        if self.record == "New":
            new_from_json = News("News", p_rec["text"], p_rec["city"])
            new_from_json.add_to_feed()
        elif self.record == "Add":
            add_from_json = Ads("Privat ad", p_rec["text"], p_rec["expiration_date"])
            add_from_json.add_to_feed()
        else:
            rec_from_json = Rec("Recipe", p_rec["text"])
            rec_from_json.add_to_feed()

    def parc(self):  # parse json file
        self.verify_file()
        if self.type_verify == 1:
            with open(self.path) as f:
                self.data = json.load(f)
            if "Records" in self.data:
                for rec in self.data["Records"]:
                    self.parse_record(rec)
            else:
                self.parse_record(self.data)
            os.remove(self.path)  # if success - delete file


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
