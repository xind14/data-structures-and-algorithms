# Stack Queue Brackets

Multi-bracket Validation.

1. Write a function called validate brackets
   - Arguments: string
   - Return: boolean
     - representing whether or not the brackets in the string are balanced
2. There are 3 types of brackets:

   - Round Brackets : ()
   - Square Brackets : []
   - Curly Brackets : {}

## Whiteboard Process

  <!-- Embedded whiteboard image -->

![Whiteboard Image](whiteboard13.png)

## Approach & Efficiency

1. Write out problem statement
2. looked at pseudoqueue code for help
3. create a dictionary of brackets
4. check key value pair, return true if there, false if not
5. The Big O time is O(n) because iterates over each character once. Space: O(n) because its dependent on input string

## Solution

![Solution Image](solution13.png)

[Link to code](https://replit.com/@XinDeng/code-challenges-401)
