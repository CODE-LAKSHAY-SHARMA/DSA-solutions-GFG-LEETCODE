"""
Print N to 1 times 
"""


def display(i, n) -> None:
    if n < i:
        return
    print(n)
    display(i, n - 1)


user = int(input("enter the number till you want to print the number from 1 "))
display(1, user)

print()
print()
print()
print()

# other approach


def func(i):
    if i == 1:
        return
    print(i)
    func(i - 1)


func(6)
