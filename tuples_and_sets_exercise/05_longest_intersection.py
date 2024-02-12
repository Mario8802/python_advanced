
n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split('-')
    first_start, first_end = [int(x) for x in first_range.split(',')]
    second_start, second_end = [int(x) for x in second_range.split(',')]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")



--------------------------------------------------------------------------------------------------------------------



longest_intersection = set()

for _ in range(int(input())):
    first_data, second_data = [el.split(",") for el in input().split("-")]  # "0,3-1,2" -> ["0,3", "1,2"] -> [["0", "3"], ["1", "2"]]

    first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))  # {0, 1, 2, 3}
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))  # {1, 2}

    intersection = first_set.intersection(second_set)  # first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is "
    f"[{', '.join(str(x) for x in longest_intersection)}] "
    f"with length {len(longest_intersection)}"
)
