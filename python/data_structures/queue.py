from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
       self.front=None
       self.back=None

    # adds item to back of queue
    def enqueue(self,value):
        new_node=Node(value)
        if self.front is None:
            self.front=new_node
            self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        value =self.front.value
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return value
    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value
#     def is_empty():

