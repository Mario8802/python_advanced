n = int(input())
reservations = set()

for _ in range(n):
    rev_number = input()
    reservations.add(rev_number)
guests = input()
while guests != "END":
    reservations.remove(guests)
    guests = input()

print(len(reservations))

for num in sorted(reservations):
    print(num)