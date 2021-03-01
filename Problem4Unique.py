# james jack
# 2/24/21

# Problem 4: Write a Python function that takes a list of numbers
# and returns a new list with unique elements of the first list.
# Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def uniq_list(x):  # creates func uniq list
    a_list = []  # creates list
    for a in x: # if a number is found in the list
        if a not in a_list:
            a_list.append(a)  # if there are duplicates, they are to be removed
    return a_list  # returns function to caller, so there is no "none" after numbers


print(uniq_list([1, 3, 3, 3, 6, 2, 3, 5]))
