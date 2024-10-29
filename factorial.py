"""
Using recursion -> print the factorial of a give number
"""


def factorial(num):
    # if num == 0:  # 0 factorial bhi 1 hota hai toh return 1 kar do
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


x = factorial(0)
print(x)  # give error if factorial(0) as condition say num==1
# phir humko condition change karke num==1 or num==0 karna hoga
