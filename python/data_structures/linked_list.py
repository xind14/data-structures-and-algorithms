class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
    - head: Points to the first node in the linked list.

    Methods:
    - __init__(): Initializes an empty linked list with a null head.
    - insert(value): Inserts a new node with the given value at the head of the list.
    - includes(value): Checks if a node with the specified value exists in the linked list.
    - __str__(): Returns a string representation of the linked list in the format "{ value1 } -> { value2 } -> ... -> NULL".
    """

    def __init__(self):
        self.head = None

    def insert (self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        result += "NULL"
        return result


class TargetError:
    pass
