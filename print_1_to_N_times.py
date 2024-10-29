"""
Print 1 to N time 
"""


def display(i, n) -> None:
    if i > n:
        return
    print(i)
    display(i + 1, n)


user = int(input("enter the number till you want to print the number from 1 "))
display(1, user)
