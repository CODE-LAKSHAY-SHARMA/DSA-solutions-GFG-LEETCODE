"""
Question 1 : calculate power of a given number which has base and it power as
 argument

"""

# ITERATIVE BASIC WAY


def power(base, power):
    return base**power


print(power(5, 3))


print()
print()
print()
# USING RECURSSION


def func(base, power):
    if power == 0:
        return base
    return base * func(base, power - 1)


print(func(5, 3))
