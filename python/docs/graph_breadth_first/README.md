# Graph Breadth First 

Write a function that LEFT JOINs two hashmaps into a single data structure. 

- Arguments: two hash maps 
  - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values. 
  - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values. 
- Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Whiteboard Process

  <!-- Embedded whiteboard image -->

![Whiteboard Image](whiteboard33.png)

## Approach & Efficiency

1. Write out problem statement
2. reviewed what hashtable import did
3. write test cases
4. drew diagram
5. asked gpt how to get back a list of list inside
6. The Big O Time: O(n log n) due to the sorting. Space: O(n) because it depends on how many keys

## Solution

[Solution](../../code_challenges/hashtable_left_join.py)
