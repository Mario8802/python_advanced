n = int(input())

unique_usernames = set()

for _ in range(n):
    unique_usernames.add(input())

print(*unique_usernames, sep="\n")


--------------------------------------------------------

print(*{input() for _ in range(int(input()))}, sep="\n")


---------------------------------------------------------


# solution 2
# names_count = int(input())
# names = set()
#
# for _ in range(names_count):
#     names.add(input())
#
# print(*names, sep="\n")
