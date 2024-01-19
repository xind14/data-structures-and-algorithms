
# Stack and Queue

- Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

1. Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

2. Stack: Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    - This object should be aware of a default empty value assigned to top when the stack is created.
        - The class should contain the following methods:
          - **push**
            - Arguments: value
            - Adds a new node with that value to the top of the stack with an O(1) Time performance.
          - **pop**
            - Arguments: none
            - Returns: the value from the node from the top of the stack
            - Removes the node from the top of the stack
            - Should raise an exception when called on an empty stack
          - **peek**
            - Arguments: none
            - Returns: Value of the node located at the top of the stack
            - Should raise an exception when called on an empty stack
          - **is empty**
            - Arguments: none
            - Returns: Boolean indicating whether or not the stack is empty.

3. Queue: Create a Queue class that has a front property. It creates an empty Queue when instantiated.
    - This object should be aware of a default empty value assigned to front when the queue is created.
    - The class should contain the following methods:
      - **enqueue**
        - Arguments: value
        - Adds a new node with that value to the back of the queue with an O(1) Time performance.
      - **dequeue**
        - Arguments: none
        - Returns: the value from the node from the front of the queue
        - Removes the node from the front of the queue
        - Should raise an exception when called on an empty queue
      - **peek**
        - Arguments: none
        - Returns: Value of the node located at the front of the queue
        - Should raise an exception when called on an empty queue
      - **is empty**
        - Arguments: none
        - Returns: Boolean indicating whether or not the queue is empty

  *You have access to the Node class and all the properties on the Linked List class.*


## Whiteboard Process
<!-- Embedded whiteboard image -->
None

## Approach & Efficiency

1. Start off writing start def functions for all four for each stack and queue
2. looked at linked list for help
3. change code to fit stack and queue properties


## Solution

None
No Link to code
