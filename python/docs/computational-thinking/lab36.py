def sum_of_elements(root):
    if not root:
        return 0

    total_sum = 0
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        total_sum += current_node.val

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return total_sum
