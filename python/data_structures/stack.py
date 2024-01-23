# from data_structures.linked_list import LinkedList
from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    A simple implementation of a Stack using a linked list.

    Attributes:
    - top: Points to the top of the stack.

    Methods:
    - push(value): Adds an item to the top of the stack.
    - pop(): Removes an item from the top of the stack.
    - peek(): Returns the value of the item located at the top of the stack without removing it.
    - is_empty(): Checks if the stack is empty.
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Adds an item to the top of the stack.

        Parameters:
        - value: The value to be added to the stack.
        """
        new_top = Node(value)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        """
        Removes an item from the top of the stack.

        Returns:
        - The value of the item removed from the top of the stack.

        Raises:
        - InvalidOperationError: If pop is called on an empty stack.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on an empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """
        Returns the value of the item located at the top of the stack without removing it.

        Returns:
        - The value of the item at the top of the stack.

        Raises:
        - InvalidOperationError: If peek is called on an empty stack.
        """
        if self.top is None:
            raise InvalidOperationError("Method not allowed on an empty collection")
        return self.top.value

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        return self.top is None
