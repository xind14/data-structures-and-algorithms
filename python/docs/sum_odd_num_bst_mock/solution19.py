class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_of_odds(root):
    sum_odd = 0
    stack = []
    current = root 

    if not current:
        return []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        
        if current.value % 2 != 0:
            sum_odd += current.value

        current = current.right

    return sum_odd
