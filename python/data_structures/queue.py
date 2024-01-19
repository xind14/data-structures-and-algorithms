from data_structures.linked_list import Node
# from data_structures.invalid_operation_error import InvalidOperationError

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
       self.front=None
       self.back=None

    # adds item to back of queue
    def enqueue(self,value):
        new_front=Node(value)
        new_front.next=self.front
        self.front=new_front
#     def dequeue():
#     def peek():
#     def is_empty():

