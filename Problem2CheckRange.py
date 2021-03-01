# james jack
# 2/24/21

# Problem 2: Write a Python function to check whether a number is in a given range.
# Use range(1,10).
# Print whether the number is in or not in the range.

def the_range(x):  # creates function
    if x in range(1, 10):
        print("this is inside the range of 1-10 ")
    else:
        print("this is not in the range of 1-10 ")


n = int(input("what number would you like tp check if it is in the range of 1-10?: "))  # input is number to be used
the_range(n)
