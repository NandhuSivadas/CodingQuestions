pairs = {'[': ']', '(': ')'}

def para(string):
    stack = []
    for ch in string:
        if ch in pairs:  
            stack.append(ch)
        else: 
            if not stack:
                return False
            top = stack.pop()
            if pairs[top] != ch:
                return False
    return not stack  

string = "([])"
print(para(string))  
