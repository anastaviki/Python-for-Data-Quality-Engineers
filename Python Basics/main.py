# Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console

#import module random
import random

if __name__ == '__main__':
#initialise variables for our list
    start = 0
    end = 1000
    quantity = 100
# create list of 100 values with random values from 0 to 1000
    list = [random.randint(start, end) for x in range(quantity)]
# print list before sorting
    print("List before sorting: ", list)
# request for input to chose type of sorting
    print("""
    Select type of sort:
    1 - bubble sort
    2 - cocktail sort
    3 - selection sort""")

    sort_type = input()
# check input and if it is not valid request for input again
    while sort_type.isalpha() or int(sort_type) <= 0 or int(sort_type) > 3:
        print('Please, check sort type, select 1,2 or 3')
        sort_type = input()

#use if for select branch to sort list using selected type of sort
    if sort_type == '1':
#bubble sort
        for i in range(quantity - 1): #outer loop for next iteration of comparation
            for j in range(quantity - i - 1): #inner loop to compare 2 adjacent standing numbers
                if list[j] > list[j + 1]: #compare values
                    list[j], list[j + 1] = list[j + 1], list[j] #swap numbers if left is greater than right

        print("Bubble sort result:", list)

    elif sort_type == '2':
# cocktail sort
        left = 0
        right = len(list) - 1
        while left <= right: #loop while left border less or equal than right
            for i in range(left, right, 1): # loop to compare 2 adjacent standing numbers - direct direction
                if list[i] > list[i + 1]: # compare values
                    list[i], list[i + 1] = list[i + 1], list[i] # swap numbers if left is greater than right
            right -= 1 # move right border

            for i in range(right, left, -1): # loop to compare 2 adjacent standing numbers - reverse direction
                if list[i - 1] > list[i]: # compare values
                    list[i], list[i - 1] = list[i - 1], list[i] # swap numbers if left is greater than right
            left += 1 # move left border
        print("Coctail sort result:", list)

    elif sort_type == '3':
#selection sort
        for i in range(len(list)): # outer loop for find min values for all iterations
            min_value_pos = i
            for item_pos in range(i, len(list)): # inner loop to find min value position for 1 iteration
                if list[min_value_pos] > list[item_pos]: # compare values
                    min_value_pos = item_pos # new min value position for 1 iteration
            list[i], list[min_value_pos] = list[min_value_pos], list[i] # swap value from current position from outer loop and min value

        print("Selection sort result:", list)

#initialise variables for average calculation
    even_sum = 0
    odd_sum = 0
    even_count=0
    odd_count=0
    for i in list: # loop on all values from the list
        if i%2 == 0: # check is even
            even_count +=1 # counter of even values
            even_sum +=i # sum of even values
        else: # for odd values
            odd_count +=1 # counter of add values
            odd_sum +=i # sum of odd values
# calculate average for even values, use try except for case if there is no even values in the list
    try:
        even_avg=even_sum/even_count
        # use formatting for better readability - output a float number with three decimal places
        print ('Everage value for all even numbers in list:  %.3f' %even_avg)
    except ZeroDivisionError:
        print ('There is no even numbers in list')
# calculate average for odd values, use try except for case if there is no odd values in the list
    try:
        odd_avg=odd_sum/odd_count
        # use formatting for better readability - output a float number with three decimal places
        print('Everage value for all odd numbers in list: %.3f' %odd_avg)
    except ZeroDivisionError:
        print ('There is no odd numbers in list')

