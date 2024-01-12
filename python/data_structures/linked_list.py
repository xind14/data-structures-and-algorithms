class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    """
    Put docstring here
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
