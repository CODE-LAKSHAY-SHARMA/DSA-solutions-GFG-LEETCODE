#  creating the node


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node | None = None  # Allow next to be Node or None


n1 = Node(5)
n2 = Node(10)
n3 = Node(15)

n1.next = n2
n2.next = n3

print(n1.next.next)
# print(n2)
