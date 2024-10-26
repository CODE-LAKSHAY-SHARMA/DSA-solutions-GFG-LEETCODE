"""
Palindrome number : 121 or 555 or nitin, mom etc
Reverse is palindrome
"""


def palindrome_number(num) -> bool:
    # cannot covert to string
    result = 0
    n = num
    while n > 0:
        remainder = n % 10
        result = (result * 10) + remainder
        n = n // 10
    if result == num:
        return True
    else:
        return False


val = palindrome_number(12344321)
print(val)

# time complexity ->  O(log 10 N)
# space complexity ->  O(1)
