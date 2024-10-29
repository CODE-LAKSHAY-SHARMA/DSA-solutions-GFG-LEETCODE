"""
Print name upto N times
"""

# using ITERATIVE APPROACH


def name1(start: int, user_input: int) -> None:
    for i in range(1, user_input):
        print("lakshay")


name1(1, 6)
print()
print()
print()


# solving through RECURSION
def name2(start: int, user_input: int) -> None:
    if start > user_input:
        return
    print("lakshay")
    name2(start + 1, user_input)  # recursive approach


name2(1, 4)
