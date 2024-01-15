n, m = (int(x) for x in input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())
common_elements = n_set & m_set
print("\n".join(common_elements))



----------------------------------------------------------------




n, m = [int(x) for x in input().split()]  # "4 3" -> ["4", "3"] -> [4, 3]

first_set = {input() for _ in range(n)}   # 1, 3, 5, 7
second_set = {input() for _ in range(m)}  # 3, 4, 5

print(*first_set.intersection(second_set), sep="\n")  # 3, 5

# print(first_set & second_set)  # and, intersection
# print(first_set | second_set)  # or, union
# print(first_set - second_set)  # subtract, difference
# print(first_set ^ second_set)  # symmetric difference
