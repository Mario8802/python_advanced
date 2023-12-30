# data = input().split(', ')
# rows = int(data[0])
# cols = int(data[1])
# # slow version
# matrix = []
# for _ in range(rows):
#     elements = [int(el) for el in input().split(',')]
#     matrix.append(elements)
#
# sum_nums = 0
#
# for row_index in range(rows):
#     for col_index in range(cols):
#         sum_nums += matrix[row_index][col_index]
#
# print(sum_nums)
# print(matrix)

#faster version
data = input().split(', ')
rows = int(data[0])
cols = int(data[1])

matrix = []
sum_nums = 0
for _ in range(rows):
    elements = [int(el) for el in input().split(',')]
    sum_nums += sum(elements)
    matrix.append(elements)

print(sum_nums)
print(matrix)