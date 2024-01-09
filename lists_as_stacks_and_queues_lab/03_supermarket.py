from collections import deque
list_of_customers = deque()
names_of_customers = input()

while names_of_customers != "End":
    if names_of_customers == "Paid":
        while list_of_customers:
            print(list_of_customers.popleft())
    else:
        list_of_customers.append(names_of_customers)
    names_of_customers = input()

print(f"{len(list_of_customers)} people remaining.")
