# Replace ___ with code

# collection of operators
operators = set(['+', '*'])  

# dictionary with operators and its precedence
precedence = {'+': 1, '*': 2} 
 
def infix_to_postfix(infix): 
    operator_stack = []
    postfix = ""
    for char in infix:
        if char not in operators:
            postfix += char
        else:
            while operator_stack and precedence[char] <= precedence[operator_stack[-1]]:
                postfix += operator_stack.pop()
            operator_stack.append(char)
                
    while operator_stack:
        postfix += operator_stack.pop()

    return postfix

expression = input()
print(infix_to_postfix(expression))
