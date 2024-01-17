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
     - append(value): Adds a new node with the given value to the end of the list.
    - insert_before(value, new_value): Inserts a new node with the specified new_value before the node with the given value.
    - insert_after(value, new_value): Inserts a new node with the specified new_value after the node with the given value.
    """

    def __init__(self):
        self.head = None

    def insert (self, value):
        # adds new node to beginning of list
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

# linked_list = LinkedList()

# linked_list.insert(3)
# linked_list.insert(7)
# linked_list.insert(10)

# print(linked_list)

    def append(self, value):
            # adds new node to end of list
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next

                current.next = new_node

    def insert_before(self, value, new_value):
        if self.head is None:
            raise TargetError("Empty list, unable to insert before")

        if self.head is not None and self.head.value == value:
            self.insert(new_value)
            return

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is None:
            raise TargetError(f"Value {value} is not in linked list")

        new_node = Node(new_value)
        new_node.next = current.next
        current.next= new_node


    def insert_after(self, value, new_value):
        if self.head is None:
            raise TargetError("Empty list unable to insert after")

        current = self.head
        while current is not None and current.value != value:
            current = current.next

        if current is None:
            raise TargetError(f"Value {value} is not in linked list")

        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node


class TargetError (Exception):
    def __init__(self, message):
        self.message = message

