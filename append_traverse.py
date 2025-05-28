class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Node | None = None  # Allow next to be Node or None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if self.head is None:
            print("Singly linkedlist is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val)
                current = current.next

    def inserthead(self, val):
        new_node = Node(val)
        if self.head is None:
            new_node = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAt(self, val, position):
        new_node = Node(val)
        current = self.head
        prev = None
        count = 0

        while current is not None and count < position:
            prev = current
            current = current.next
            count = count + 1
        new_node.next = current
        prev.next = new_node

    def deleteHead(self):
        if self.head is None:
            print("Cannot delete the head at is empty")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def deleteVal(self, val):
        if self.head.val == val:
            self.deleteHead()
            print("Empty")
        else:
            current = self.head
            prev = None
            while current.val != val and current:
                prev = current
                current = current.next
            if current is None:
                print(f"Value {val} not found in the list")

            prev.next = current.next
            del current


s1 = SinglyLinkedList()

s1.append(10)
s1.append(20)
s1.append(30)
s1.append(40)
# s1.traverse()
s1.insertAt(100, 2)
# s1.traverse()
s1.deleteVal(100)
s1.traverse()
