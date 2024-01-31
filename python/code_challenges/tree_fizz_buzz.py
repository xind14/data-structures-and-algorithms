from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    if not tree.root:
        return None
    
    def determine_fizz_buzz(value):
        if value % 3 ==0:
            return "Fizz"
        elif value % 5 ==0:
            return "Buzz"
        elif value % 3 ==0 and value % 5 ==0 :
            return "FizzBuzz"
        else:
            return str(value)
    
    def determine_new_tree(node):
        new_node=Node(determine_fizz_buzz(node.value))
        for child in tree.root.children:
            new_child=fizz_buzz_tree(KaryTree(child))
            new_node.children.append(new_child.root)
        return KaryTree(new_node)