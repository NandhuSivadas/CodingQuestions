def calculate(s):
    s = s.replace(' ', '')

    i = 0
    num = 0
    sign = 1
    result = 0
    stack = []  # stack stores previous (result, sign)

    while i < len(s):
        ch = s[i]

        if ch.isdigit():
            num = num * 10 + int(ch)

        elif ch in '+-':
            result += sign * num
            num = 0
            sign = 1 if ch == '+' else -1

        elif ch == '(':
         
            stack.append((result, sign))
         
            result = 0
            sign = 1
            num = 0

        elif ch == ')':
         
            result += sign * num
          
            prev_result, prev_sign = stack.pop()
          
            result = prev_result + (prev_sign * result)
            num = 0
            sign = 1

        i += 1

    return result + sign * num