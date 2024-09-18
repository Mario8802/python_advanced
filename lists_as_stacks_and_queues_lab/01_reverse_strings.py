# some_text = list(input())

# while some_text:
#     print(some_text.pop(),end="")


some_string = input()

my_stack = []

for i in some_string:
    my_stack.append(i)

while my_stack:
    print(my_stack.pop(), end='')
