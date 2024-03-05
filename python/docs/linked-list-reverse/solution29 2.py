def reverse_list(self):
    prev_node=None
    current_node=self.head
    
    while current_node:
        next_node=current_node.next
        current_node.next=prev_node
        prev_node=current_node
        current_node=next_node
    return prev_node
            



class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
