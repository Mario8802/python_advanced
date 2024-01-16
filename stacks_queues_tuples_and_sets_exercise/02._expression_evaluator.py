from collections import deque

expression = input().split()
numbers = deque()

for char in expression:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if char == '+':
                numbers.appendleft(first_num + second_num)
            elif char == '-':
                numbers.appendleft(first_num - second_num)
            elif char == '*':
                numbers.appendleft(first_num * second_num)
            elif char == '/':
                numbers.appendleft(first_num // second_num)


print(numbers[0])

2.1

# from collections import deque
#
# expression = input().split()
# numbers = deque()
#
# for char in expression:
#     if char not in '+-*/':
#         numbers.append(int(char))
#     else:
#         while len(numbers) > 1:
#             first_num = numbers.popleft()
#             second_num = numbers.popleft()
#             if char == '+':
#                 numbers.appendleft(first_num + second_num)
#             elif char == '-':
#                 numbers.appendleft(first_num - second_num)
#             elif char == '*':
#                 numbers.appendleft(first_num * second_num)
#             elif char == '/':
#                 numbers.appendleft(first_num // second_num)
#
#
# print(numbers[0])


from collections import deque

expression = input().split()
numbers = deque()

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for char in expression:
    if char not in '+-*/':
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()     
         
            numbers.appendleft(operators[char](first_num, second_num))

print(numbers[0])


----------------------------------------------------------------------------------
from collections import deque
from math import floor

expression = deque(input().split())  # [6, 5, -, 4, 5, +]

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element == "*":
        for _ in range(idx - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "/":
        for _ in range(idx - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == "-":
        for _ in range(idx - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "+":
        for _ in range(idx - 1):  # -1 -> everything but the symbol
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in "/*+-":
        del expression[1]
        idx = 1

    idx += 1

print(floor(int(expression[0])))
--------------------------------------------------------------------------------------
from functools import reduce
from math import floor

expression = input().split()  # [6, 5, 4, 5, +]

idx = 0
# TODO: debug
functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
}

# [1, 2, +, 4, 5, -]
# [3, 4, 5, -]

while idx < len(expression):
    element = expression[idx]

    if element in "/*+-":
        expression[0] = functions[element](idx)
        [expression.pop(1) for _ in range(idx)]  # pop everything including the symbol
        idx = 1

    idx += 1

print(floor(int(expression[0])))
------------------------------------------------------------------------------------
from collections import deque
from math import floor

expression = deque(input().split())  # [6, 5, -, 4, 5, +]

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element in "/*+-":
        for _ in range(idx - 1):
            expression.appendleft(eval(f"{expression.popleft()} {element} {expression.popleft()}"))

        del expression[1]
        idx = 1

    idx += 1

print(floor(int(expression[0])))
