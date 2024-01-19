# from data_structures.linked_list import LinkedList
from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top=None
    # add to front of stack 
    def push(self,value):
        new_top=Node(value)
        new_top.next=self.top
        self.top=new_top

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value


    def peek(self):
         if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
         return self.top.value


    def is_empty(self):
        return self.top is None


