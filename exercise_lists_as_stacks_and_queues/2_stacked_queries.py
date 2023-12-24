n = int(input())
stacked_queries = []

for _ in range(n):
    query = input().split()
    if query[0] == "1":
        stacked_queries.append(int(query[1]))
    elif stacked_queries:
        if query[0] == "2":
            stacked_queries.pop()
        elif query[0] == "3":
            print(max(stacked_queries))
        elif query[0] == "4":
            print(min(stacked_queries))

while stacked_queries:
    print(stacked_queries.pop(), end="")
    if stacked_queries:
        print(", ", end="")