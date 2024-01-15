n = int(input())
odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name_sum = sum([ord(char) for char in input()]) // i
    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
elif sum(even_set) < sum(odd_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)
print(*result, sep=', ')


-------------------------------------------------------------------------------------------


odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(l) for l in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)
    else:
        odd_set.add(ascii_sum_of_name)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=", ")  # B - A
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
