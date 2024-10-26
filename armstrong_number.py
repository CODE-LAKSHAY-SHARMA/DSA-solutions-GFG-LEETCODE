"""
Armstrong number:  153 -> (1)^3 + (5)^3 + (3)^3
"""


def armstrong_number(num) -> bool:
    n = num
    b = str(num)
    length = len(b)
    # other way to find the length
    # len2=int(math.log10(num))+1
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit**length
        n = n // 10
    if sum == num:
        return True
    else:
        return False


a = 153
val = armstrong_number(a)
print(val)

# time complexity ->  O(log 10 N)
# space complexity ->  O(1)
