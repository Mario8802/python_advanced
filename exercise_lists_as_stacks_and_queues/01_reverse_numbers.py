n = input().split()
stack = []
for i in range(len(n)):
    stack.append(n[i])
print(*stack[::-1],end=" ")