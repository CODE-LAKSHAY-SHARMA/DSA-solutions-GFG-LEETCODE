"""
Sum of N Natural Number using recurssion two method

1.  parametrised method
2. function methods
"""

# def func(i, sum=0):
#     if i < 0:
#         print(sum)
#         return
#     func(i - 1, sum + i)  # backtracking concept using recursion

# func(5)


# function Methods
"""
2 step 

1. make the flow of the code
2. Calculate the base case 
"""


def func(num):
    if num == 1:
        return 1
    return num + func(num - 1)


print(func(5))
