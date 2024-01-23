from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    A simple implementation of a Queue using a linked list.

    Attributes:
    - front: Points to the front of the queue.
    - rear: Points to the back of the queue.

    Methods:
    - enqueue(value): Adds an item to the back of the queue.
    - dequeue(): Removes an item from the front of the queue.
    - peek(): Returns the value of the item located at the front of the queue without removing it.
    - is_empty(): Checks if the queue is empty.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Adds an item to the back of the queue.

        Parameters:
        - value: The value to be added to the queue.
        """
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Removes an item from the front of the queue.

        Returns:
        - The value of the item removed from the front of the queue.

        Raises:
        - InvalidOperationError: If dequeue is called on an empty queue.
        """
        if self.front is None:
            raise InvalidOperationError("Method not allowed on an empty collection")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek(self):
        """
        Returns the value of the item located at the front of the queue without removing it.

        Returns:
        - The value of the item at the front of the queue.

        Raises:
        - InvalidOperationError: If peek is called on an empty queue.
        """
        if self.front is None:
            raise InvalidOperationError("Method not allowed on an empty collection")
        return self.front.value

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
        - True if the queue is empty, False otherwise.
        """
        return self.front is None
