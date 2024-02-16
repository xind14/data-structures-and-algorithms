from data_structures.stack import Stack

def multi_bracket_validation(input_str):
    stack = Stack()
    brackets = {'(': ')', '[': ']', '{': '}'}

    for char in input_str:
        if char in brackets.keys():
            stack.push(char)
        elif char in brackets.values():
            if stack.is_empty() or brackets[stack.pop()] != char:
                return False
        else:
            continue

    return stack.is_empty()

