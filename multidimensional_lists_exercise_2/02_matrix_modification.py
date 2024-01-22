rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if row < 0 or row >= rows or col < 0 or col >= rows:
        print("Invalid coordinates")
        continue
    if command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract" :
        matrix[row][col] -= value
for row in matrix:
    print(*row, sep=' ')


-----------------------------------------------------------------------


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":
    type_command, r, c, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= r < size and 0 <= c < size):
        print("Invalid coordinates")
    elif type_command == "Add":
        matrix[r][c] += number
    elif type_command == "Subtract":
        matrix[r][c] -= number

    command = input().split()

[print(*row) for row in matrix]
