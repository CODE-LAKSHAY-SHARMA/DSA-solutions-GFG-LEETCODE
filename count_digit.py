"""
Count digit problem with brute force and optimal approach 
concept of LOG 
"""

# brute force method
import math


def count_digit(n) -> int:
    count = 0
    num = n
    while num > 0:
        count += 1
        num = num // 10
    return count


val = count_digit(57819)
print(f"Brute Force method to count digits->  {val}")
print("the time complexity is -> O(log N)")

# optimal method  which give complexity with O(1)


def count_digit2(num1):
    return math.floor(math.log10(num1)) + 1


print(count_digit2(57819))
