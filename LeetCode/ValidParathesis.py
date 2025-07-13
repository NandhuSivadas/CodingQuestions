def balanced():
    expr = input("Enter the expression: ") 
    stack = []

    for char in expr:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return not stack  
print(balanced())