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
