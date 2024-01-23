from data_structures.stack import Stack


class PseudoQueue:
    """
        A pseudo-queue implemented using two stacks.

        Attributes:
            stack1 (Stack): The main stack for enqueueing elements.
            stack2 (Stack): The other stack for dequeuing elements.
    """

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()





