from data_structures.binary_tree import BinaryTree, Node

def tree_intersection(tree1, tree2):
    # Initialize hash table to store values of tree1
    hashtable = {}

    # Traverse tree1 and store its values in the hash table
    tree1_values = tree1.in_order()
    for value in tree1_values:
        hashtable[value] = True

    # Initialize a list to store common values
    common_values = []

    # Traverse tree2 and check if each value exists in the hash table
    tree2_values = tree2.in_order()
    for value in tree2_values:
        if hashtable.get(value):
            common_values.append(value)

    return list(set(common_values))  # Convert list to set to remove duplicates, then back to list


# from data_structures.binary_tree import BinaryTree


# def tree_intersection(root1, root2):
#     values_dict = {}
#     queue = []
#     queue.append(root1.root)
#     while queue:
#         node = queue[0]
#         queue = queue[1:]
#         values_dict[node.value] = True
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

#     common_values = set()
#     queue = []
#     queue.append(root2.root)
#     while queue:
#         node = queue[0]
#         queue = queue[1:]
#         if node.value in values_dict:
#             common_values.add(node.value)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

#     return common_values