# Description
# Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
#
# 1.Define your input format (one or many records)
#
# 2.Default folder or user provided file path
#
# 3.Remove file if it was successfully processed

from gui import *
from csv_create import *  # import module for statistics
from parsing_and_adding import *

window = Window("Add Publications", "Select Type of Publication")
window.show_window()  # add window for select type of publication
type_of_pub = window.input_type
# open window with adding new publications until exit from the app
success = 1
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
    elif type_of_pub == "Provide records with file":
        add_file = WindowAddFromFile("Add records with file", "Select file")
        add_file.show_window()
        par = ParcerFile(add_file.filename, "Records")
        par.parc()
        if par.type_verify == 0:
            success = 0
    elif type_of_pub == "Provide New with file":
        add_file = WindowAddNewFromFile("Add new with file", "Select file")
        add_file.show_window()
        par = ParcerFile(add_file.filename, "New")
        par.parc()
        if par.type_verify == 0:
            success = 0
    elif type_of_pub == "Provide Private ad with file":
        add_file = WindowAddAddFromFile("Add Add", "Select file")
        add_file.show_window()
        par = ParcerFile(add_file.filename, "Add")
        par.parc()
        if par.type_verify == 0:
            success = 0
    elif type_of_pub == "Provide Recipe with file":
        add_file = WindowRecipeFromFile("Add Recipe", "Select file")
        add_file.show_window()
        par = ParcerFile(add_file.filename, "Recipe")
        par.parc()
        if par.type_verify == 0:
            success = 0

    elif type_of_pub == "Provide records with json":
        add_file = WindowRecordsFromJson("Add Records", "Select file")
        add_file.show_window()
        par = ParserJson(add_file.filename, "Records")
        par.parc()
        if par.type_verify == 0:
            success = 0
    elif type_of_pub == "Provide New with json":
        add_file = WindowNewFromJson("Add New", "Select file")
        add_file.show_window()
        par = ParserJson(add_file.filename, "New")
        par.parc()
        if par.type_verify == 0:
            success = 0

    elif type_of_pub == "Provide Private ad with json":
        add_file = WindowAddFromJson("Add Add", "Select file")
        add_file.show_window()
        par = ParserJson(add_file.filename, "Add")
        par.parc()
        if par.type_verify == 0:
            success = 0
    else:
        add_file = WindowRecipeFromJson("Add Recipe", "Select file")
        add_file.show_window()
        par = ParserJson(add_file.filename, "Recipe")
        par.parc()
        if par.type_verify == 0:
            success = 0

    if success == 1:  # if succesfully
        window = Window("Add Publications", "Successfully added, Select Type of Publication")
        statistics = Statistics('newsfeed.txt')  # create class for recalculate statistics
        statistics.read_file()
        statistics.calculate_add_word_stat()
        statistics.calculate_letter_stat()
    else:
        window = Window("Add Publications", "Check your input  and Select Type of Publication", 1)
    window.show_window()
    type_of_pub = window.input_type

    success = 1
