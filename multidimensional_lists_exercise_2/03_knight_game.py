n = int(input())
matrix = []
knights = []

for row in range(n):
    matrix.append([(x)for x in input()])
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])

removed_knights = 0
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2),(-2, -1)]

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if 0 <= new_row < n and 0 <= new_col < n:
                if matrix[new_row][new_col] == 'K':
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break
    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = '0'
    removed_knights += 1

print(removed_knights)


-----------------------------------------------------------------------------------------------------


size = int(input())
matrix = [list(input()) for _ in range(size)]

pos_numbers = [-2, -1, 1, 2]
positions = [(x, y) for x in pos_numbers for y in pos_numbers if abs(x) != abs(y)]
# positions = (
#     (-2, -1),  # горе 2, ляво 1
#     (-2, 1),   # горе 2, дясно 1
#     (-1, -2),  # горе 1, ляво 2
#     (-1, 2),   # горе 1, дясно 2
#     (2, 1),    # долу 2, дясно 1
#     (2, -1),   # долу 2, ляво 1
#     (1, -2),   # долу 1, ляво 2
#     (1, 2),    # долу 1, ляво -2
# )

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []  # [row, col]

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
