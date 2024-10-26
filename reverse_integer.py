# reverse integer


def reverse_integer(n) -> int:
    result = 0
    while n > 0:
        last_digit = n % 10
        result = result * 10 + last_digit
        n = n // 10
    return result


val = reverse_integer(1257)
print(val)  # Output: 7521

# time complexity ->  O(log 10 N)
# space complexity -> O(1)  # constant space complexity

# HINT  -> if the number is negative then multiply it by -1 and then make it negative at the end
# or use the abs() method  which make negative interger to positive
