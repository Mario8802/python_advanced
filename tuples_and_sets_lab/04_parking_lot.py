n = int(input())

cars = set()

for i in range(n):
    direction, number_plate = input().split(", ")
    if direction == "IN":
        cars.add(number_plate)
    elif direction == "OUT":
        if number_plate in cars:
            cars.remove(number_plate)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
