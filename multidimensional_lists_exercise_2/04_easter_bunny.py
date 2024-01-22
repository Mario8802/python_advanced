n = int(input())

matrix = []
bunny = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == 'B':
            bunny = [row, col]

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

max_eggs = float('-inf')
max_direction = ''
max_eggs_matrix = []

for direction, move in possible_moves.items():
    eggs = 0
    curr_eggs_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break
        eggs += int(matrix[row][col])
        curr_eggs_matrix.append([row, col])
        row += move[0]
        col += move[1]
    if eggs > max_eggs and curr_eggs_matrix:
        max_eggs = eggs
        max_direction = direction
        max_eggs_matrix = curr_eggs_matrix
print(max_direction)
[print(row) for row in max_eggs_matrix]
print(max_eggs)



--------------------------------------------------------------------


size = int(input())

matrix = []
bunny_pos = []  # [row, col]
best_path = []

best_direction = None
max_collected_eggs = float("-inf")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix.append(input().split())

    if 'B' in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep="\n")  # [[1, 2], [3, 4], ...]
print(max_collected_eggs)
