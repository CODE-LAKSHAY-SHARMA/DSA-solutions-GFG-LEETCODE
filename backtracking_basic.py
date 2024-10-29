"""
print 1 to N number without using i+1 in the function calling itself
"""

# backtracking  :  karte jaao jab tak condition met na ho jaaye phir print karo


def func(i):
    if i < 1:
        return
    func(i - 1)
    print(i, end=" ")


func(5)


"""
Print N to 1 using - symbol
"""


def print_n_to_1(n, current=1):
    if current > n:
        return

    print_n_to_1(n, current + 1)
    print(current)


N = 4
print_n_to_1(N)
