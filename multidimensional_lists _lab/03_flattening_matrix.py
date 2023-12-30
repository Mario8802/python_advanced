# matrix = [["M" for j in range(2)]for i in range(3)]
# print(matrix)

rows = int(input())
matrix = []

for row in range(rows):
    elements = [int(el) for el in input().split(',')]
    matrix.append(elements)

flattened = []

for row_index in range(rows):
    for col_index in range(len(matrix[row_index])):
        flattened.append(matrix[row_index][col_index])

print(flattened)