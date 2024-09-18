# expression = input()
# stack = []

# for index in range(len(expression)):
#     if expression[index] == "(":
#         stack.append(index)
#     elif expression[index] == ")":
#         start_index = stack.pop()
#         last_index = index + 1
#         print(expression[start_index:last_index])


algebraic_expression = input()

stack = []

for i, v in enumerate(algebraic_expression):
    if v == "(":
        stack.append(i)
    elif v == ")":
        if stack:  
            opening_bracket = stack.pop()
            print(algebraic_expression[opening_bracket:i + 1])
