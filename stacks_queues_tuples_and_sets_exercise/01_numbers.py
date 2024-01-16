first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + ' ' + line[1]
    numbers = [int(num) for num in line[2:]]
    if command == 'Add First':
        first_set.update(numbers)
    elif command == 'Add Second':
        second_set.update(numbers)
    elif command == 'Remove First':
        first_set.difference_update(numbers)
    elif command == 'Remove Second':
        second_set.difference_update(numbers)
    elif command == 'Check Subset':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))
print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
---------------------------------------------------------------


first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_set.add(int(el)) for el in x],  # first_set.update(second_set)
    "Add Second": lambda x: [second_set.add(int(el)) for el in x],
    "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
    "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    functions[command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
------------------------------------------------------------------------
first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    if command == "Add First":
        [first_set.add(int(el)) for el in data]
    elif command == "Add Second":
        [second_set.add(int(el)) for el in data]
    elif command == "Remove First":
        [first_set.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [second_set.discard(int(el)) for el in data]
    elif command == "Check Subset":
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
