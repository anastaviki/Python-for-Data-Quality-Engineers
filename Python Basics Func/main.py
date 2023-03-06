# Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console

# import module random
import random
import time


def timer(f):  # decorator for calculating time of execution of funcrion
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Time for executing", f.__name__, " function: %f" % (time.time()-t))
        return res

    return tmp


# initialise variables for our list
start = 0
end = 1000
quantity = 100


# create list of p_quantity values with random values from p_start to p_end
def create_random_list(p_start, p_end, p_quantity):
    return [random.randint(p_start, p_end) for x in range(p_quantity)]


# get input from user
def get_value():
    # request for input to chose type of sorting
    r_sort_type = input("""Select type of sort:
        1 - bubble sort
        2 - cocktail sort
        3 - selection sort
        """)
    return r_sort_type


# validate an input and request input from user ones more in case of incorrect value
def validate_type(p_sort_type):
    # check input and if it is not valid request for input again
    correct_type = False
    while not correct_type:  # check flag for correct type of sorting
        try:  # exception for incorrect values
            if int(p_sort_type) < 1 or int(p_sort_type) > 3:  # check validity of values
                print('Out of range')
                p_sort_type = get_value()  # ask for correct input
            else:
                correct_type = True  # change value of flag

        except ValueError:  # exception ask for input again
            print('Non numeric')
            p_sort_type = get_value()


# compare 2 values in list and swap values if needed
def compare_and_swap_values(p_list, p_pos_1, p_pos_2):
    if p_list[p_pos_1] > p_list[p_pos_2]:  # compare values
        # swap numbers if left is greater than right
        p_list[p_pos_1], p_list[p_pos_2] = p_list[p_pos_2], p_list[p_pos_1]
    return p_list


# bubble sort of list
@timer  # use decorator for calculating time of execution
def bubble_sort(p_list_for_sort):
    p_quantity = len(p_list_for_sort)
    for i in range(p_quantity - 1):  # outer loop for next comparison iteration
        for j in range(p_quantity - i - 1):  # inner loop to compare 2 adjacent standing numbers
            p_list_for_sort = compare_and_swap_values(p_list_for_sort, j, j+1)
    print("Bubble sort result: ", p_list_for_sort)


# cocktail sort of list
@timer  # use decorator for calculating time of execution
def cocktail_sort(p_list_for_sort):
    left = 0
    right = len(p_list_for_sort) - 1
    while left <= right:  # loop while left border less or equal than right
        for i in range(left, right, 1):  # loop to compare 2 adjacent standing numbers - direct direction
            p_list_for_sort = compare_and_swap_values(p_list_for_sort, i, i + 1)
        right -= 1  # move right border

        for i in range(right, left, -1):  # loop to compare 2 adjacent standing numbers - reverse direction
            p_list_for_sort = compare_and_swap_values(p_list_for_sort, i - 1, i)
        left += 1  # move left border
    print("Cocktail sort result: ", list_for_sort)


# find position of minimum value in list
def find_min_value_pos(p_list_for_sort, p_min_value_pos):
    # loop to find min value position in list
    for item_pos in range(p_min_value_pos, len(p_list_for_sort)):
        if p_list_for_sort[p_min_value_pos] > p_list_for_sort[item_pos]:  # compare values
            p_min_value_pos = item_pos  # new min value position for 1 iteration
    return p_min_value_pos


# selection sort
@timer  # use decorator for calculating time of execution
def selection_sort(p_list_for_sort):
    for i in range(len(p_list_for_sort)):  # outer loop for find min values for all iterations
        min_value_pos = find_min_value_pos(p_list_for_sort, i)  # find min value position in list
        # swap value from current position from outer loop and min value
        p_list_for_sort = compare_and_swap_values(p_list_for_sort, i, min_value_pos)
    print("Selection sort result: ", p_list_for_sort,)


# calculate sum and numbers for odd and even values in list
def calculate_sum_and_numbers(p_list_for_sort):

    try:
        # calculate and print average for even numbers
        print('Average value for all even numbers in list:  %.3f'
              % (sum([v for k, v in enumerate(p_list_for_sort) if v % 2 == 0]) /
                 sum([1 for k, v in enumerate(p_list_for_sort) if v % 2 == 0])))
    except ZeroDivisionError:
        print('There is no even numbers in list')
    try:
        # calculate and print average for odd numbers
        print('Average value for all odd numbers in list:  %.3f'
              % (sum([v for k, v in enumerate(p_list_for_sort) if v % 2 == 1]) /
                 sum([1 for k, v in enumerate(p_list_for_sort) if v % 2 == 1])))
    except ZeroDivisionError:
        print('There is no odd numbers in list')


list_for_sort = create_random_list(start, end, quantity)
# print list before sorting
print("List before sorting: ", list_for_sort)
sort_type = get_value()

validate_type(sort_type)
# use if for select branch to sort list using selected type of sort
if sort_type == '1':
    # bubble sort
    bubble_sort(list_for_sort)

elif sort_type == '2':
    # cocktail sort
    cocktail_sort(list_for_sort)

elif sort_type == '3':
    # selection sort
    selection_sort(list_for_sort)


calculate_sum_and_numbers(list_for_sort)



