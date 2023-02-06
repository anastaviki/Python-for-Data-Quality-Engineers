# Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console

# import module random
import random


# initialise variables for our list
start = 0
end = 1000
quantity = 100
# create list of 100 values with random values from 0 to 1000
list_for_sort = [random.randint(start, end) for x in range(quantity)]
# print list before sorting
print("List before sorting: ", list)
# request for input to chose type of sorting

sort_type = input("""
    Select type of sort:
    1 - bubble sort
    2 - cocktail sort
    3 - selection sort
    """)
# check input and if it is not valid request for input again
correct_type = False

while not correct_type:  # check flag for correct type of sorting
    try:  # exception for incorrect values
        if int(sort_type) < 1 or int(sort_type) > 3:  # check validity of values
            sort_type = input('Please, check sort type, select 1,2 or 3: ')  # ask for correct input
        else:
            correct_type = True  # change value of flag

    except ValueError:  # exception ask for input again
        print('Non numeric')
        sort_type = input('Please, check sort type, select 1,2 or 3: ')

# use if for select branch to sort list using selected type of sort
if sort_type == '1':
    # bubble sort
    for i in range(quantity - 1):  # outer loop for next comparison iteration
        for j in range(quantity - i - 1):  # inner loop to compare 2 adjacent standing numbers
            if list_for_sort[j] > list_for_sort[j + 1]:  # compare values
                # swap numbers if left is greater than right
                list_for_sort[j], list_for_sort[j + 1] = list_for_sort[j + 1], list_for_sort[j]

    print("Bubble sort result:", list_for_sort)

elif sort_type == '2':
    # cocktail sort
    left = 0
    right = len(list_for_sort) - 1
    while left <= right:  # loop while left border less or equal than right
        for i in range(left, right, 1):  # loop to compare 2 adjacent standing numbers - direct direction
            if list_for_sort[i] > list_for_sort[i + 1]:  # compare values
                # swap numbers if left is greater than right
                list_for_sort[i], list_for_sort[i + 1] = list_for_sort[i + 1], list_for_sort[i]
        right -= 1  # move right border

        for i in range(right, left, -1):  # loop to compare 2 adjacent standing numbers - reverse direction
            if list_for_sort[i - 1] > list_for_sort[i]:  # compare values
                # swap numbers if left is greater than right
                list_for_sort[i], list_for_sort[i - 1] = list_for_sort[i - 1], list_for_sort[i]
        left += 1  # move left border
    print("Cocktail sort result:", list_for_sort)

elif sort_type == '3':
    # selection sort
    for i in range(len(list_for_sort)):  # outer loop for find min values for all iterations
        min_value_pos = i
        for item_pos in range(i, len(list_for_sort)):  # inner loop to find min value position for 1 iteration
            if list_for_sort[min_value_pos] > list_for_sort[item_pos]:  # compare values
                min_value_pos = item_pos  # new min value position for 1 iteration
                # swap value from current position from outer loop and min value
        list_for_sort[i], list_for_sort[min_value_pos] = list_for_sort[min_value_pos], list_for_sort[i]

    print("Selection sort result:", list_for_sort)

# initialise variables for average calculation
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
for i in list_for_sort:  # loop on all values from the list
    if i % 2 == 0:  # check is even
        even_count += 1  # counter of even values
        even_sum += i  # sum of even values
    else:  # for odd values
        odd_count += 1  # counter of add values
        odd_sum += i  # sum of odd values
# calculate average for even values, use try except for case if there is no even values in the list
try:
    even_avg = even_sum/even_count
    # use formatting for better readability - output a float number with three decimal places
    print('Average value for all even numbers in list:  %.3f' % even_avg)
except ZeroDivisionError:
    print('There is no even numbers in list')
# calculate average for odd values, use try except for case if there is no odd values in the list
try:
    odd_avg = odd_sum/odd_count
    # use formatting for better readability - output a float number with three decimal places
    print('Average value for all odd numbers in list: %.3f' % odd_avg)
except ZeroDivisionError:
    print('There is no odd numbers in list')

