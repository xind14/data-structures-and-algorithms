
# Hashtable

Branch Name: hashtable

Challenge Type: New Implementation

## Whiteboard Process

<!-- Embedded whiteboard image -->
None. Not a whiteboard

## Approach & Efficiency

1. Linked List
    - Create a Hashtable class
    - Upon instantiation, a hashtable with a specific size is set
2. The class should contain the following methods
    - set
        - Arguments: key, value
        - Returns: nothing
        - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
        - Should a given key already exist, replace its value from the value argument given to this method.
    - get
        - Arguments: key
        - Returns: Value associated with that key in the table

    - has
        - Arguments: key
        - Returns: Boolean, indicating if the key exists in the table already.
    - keys
        - Returns: Collection of keys
    - hash
        - Arguments: key
        - Returns: Index in the collection for that key

## Solution


[Link to code](../../data_structures/hashtable.py)
