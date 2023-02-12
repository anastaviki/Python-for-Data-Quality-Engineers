# Write a code, which will:
#
# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

import random  # import random module
import string  # import string module

number_of_dicts = random.randint(2, 10)  # get random number of dictionaries
list_of_dicts = []  # create empty list
start_tuple = tuple(string.ascii_lowercase)  # initialise tuple with possible keys for dicts

for i in range(number_of_dicts):  # loop for adding dict in list
    numbers_of_dict_values = random.randint(1, len(start_tuple))  # get random value of keys in dict
    temp_dict = {}  # create empty dict
    list_of_keys = (random.sample(start_tuple, numbers_of_dict_values))  # generate list of unique keys
    for j in list_of_keys:  # loop for adding values in dict
        temp_dict[j] = random.randint(0, 100)  # add key-value to dict
    list_of_dicts.append(temp_dict)  # add dict to list

print("List of dicts: ", list_of_dicts)  # print list of dictionaries

res_dict = {}  # create empty dict for result

for letter in start_tuple:  # loop for check every possible value in dicts
    max_value = -1  # initialise max value
    number_of_dict = 0  # for safe number of dict with maximum value in it
    dict_counter = 0  # for count numbers of dictionaries in with key exists
    for i in range(0, number_of_dicts):  # loop for check all dictionaries
        if letter in list_of_dicts[i]:  # check if this key exists in dictionary
            if max_value < list_of_dicts[i].get(letter):  # check if value greater than current maximum value
                max_value = list_of_dicts[i].get(letter)  # new maximum value
                number_of_dict = i + 1  # change number of dict with maximum value for specific key
            dict_counter += 1  # increase a counter of dictionaries with specific key
    if max_value == -1:  # check if max value was changed in the loop
        pass
    elif dict_counter == 1:  # check if there is only one dictionary with specific key
        res_dict[letter] = max_value  # add value to result dictionary
    else:  # if there are more than one dictionary with specific key
        res_dict[letter + '_' + str(number_of_dict)] = max_value  # add value to result dictionary
print("Resulted dict: ", res_dict)  # print result dictionary
