# Trees

Branch Name: trees

Challenge Type: New Implementation

## Whiteboard Process

<!-- Embedded whiteboard image -->

None. Not a whiteboard

## Approach & Efficiency

1. **Node**

   - Create a `Node` class that has properties for the value stored in the node, the left child node, and the right child node.

2. **Binary Tree**

   - Create a `Binary Tree` class.
     - Define a method for each of the depth-first traversals:
       1. Pre-order
       2. In-order
       3. Post-order
     - Each depth-first traversal method should return an array of values, ordered appropriately.

3. **Binary Search Tree**
   - Create a `Binary Search Tree` class.
     - This class should be a sub-class (or your language's equivalent) of the `Binary Tree` class, with the following additional methods:
       - `Add`
         - Arguments: `value`
         - Return: nothing
         - Adds a new node with that value in the correct location in the binary search tree.
       - `Contains`
         - Argument: `value`
         - Returns: boolean indicating whether or not the value is in the tree at least once.

## Solution

1. [Binary Tree Link to code](../../data_structures/binary_tree.py)
2. [Binary Search Tree Link to code](../../data_structures/binary_search_tree.py)
