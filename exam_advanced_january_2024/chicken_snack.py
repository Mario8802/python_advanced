from collections import deque


def process_transactions(money, prices):
    food_count = 0

    while money and prices:
        if money[-1] == prices[0]:
            food_count += 1
            money.pop()
            prices.popleft()
        elif money[-1] > prices[0]:
            henry_cash_difference = money[-1] - prices[0]
            food_count += 1
            money.pop()
            if money:
                money[-1] += henry_cash_difference
            prices.popleft()
        elif money[-1] < prices[0]:
            money.pop()
            prices.popleft()

    return food_count


def display_result(food_count):
    if food_count >= 4:
        print(f"Gluttony of the day! Henry ate {food_count} foods.")
    elif 4 > food_count > 1:
        print(f"Henry ate: {food_count} foods.")
    elif food_count == 1:
        print(f"Henry ate: {food_count} food.")
    else:
        print("Henry remained hungry. He will try next weekend again.")


money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())

food_count = process_transactions(money, prices)
display_result(food_count)

# Henry loves street food and he can't wait for the weekend to come because that's when he goes for a walk
# and enjoys his favorite food. His mother knows this and decides to surprise him by putting some change in
# his pants pocket.
# On the first line, you will be given a sequence of integers representing the amount of money in Henry's pocket.
# In the next line, you will be given another sequence of integers representing the prices of foods that Henry can buy.
# Henry has gone to his favorite fast food place, fumbles in his pocket and pulls out some change.
#  You have to start with the last element from the amount of money sequence and compare it with the first element
#  from the prices sequence.
#     • If their values are equal, Henry buys the food. After that, you should remove both of them from their sequences.
#     • If the amount of money is bigger than the price, he buys the food again, taking change (the difference
#     between the amount of money and the price) and putting it in his pocket. You should calculate the difference
#     between the values, and keep it.
#         ◦ Remove the current amount of money from its sequence and increase the next amount of money value in
#         the sequence by the resulting difference you have calculated.
#         ◦ Remove the price from the prices sequence.
#     • If the amount of money is lower than the price remove both of them from their sequences.
# You need to stop comparing when you have no more amounts of money or prices.
# Input / Constraints
#     • On the first line, you will receive the integers, representing the amount of money size, separated
#     by a single space.
#     • On the second line, you will receive the integers, representing the price size, separated by a single space.
#     • All given numbers will be valid integers in the range [1, 20].
# Output
#     • The output of your program should be a single line of text, formatted according to the following rules:
#     • If Henry managed to eat four or more foods print the following:
#         ◦ "Gluttony of the day! Henry ate {food count} foods."
#     • If Henry has eaten some of the foods print the following:
#     • "Henry ate: {food count} foods."
#     • in case Henry has eaten only one food, print: "Henry ate: {food count} food."
#     • If Henry has not eaten any food:
#         ◦ "Henry remained hungry. He will try next weekend again."

from collections import deque


henrys_pocket_money = [int(el) for el in input().split()]
prices_of_foods = deque(int(el) for el in input().split())

food_eaten_by_henry = 0


while henrys_pocket_money and prices_of_foods:
    current_amount = henrys_pocket_money.pop()
    prices = prices_of_foods.popleft()

    if current_amount > prices:
        if henrys_pocket_money:
            henrys_pocket_money[-1] += current_amount - prices

    elif current_amount < prices:
        continue

    food_eaten_by_henry += 1

if food_eaten_by_henry >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten_by_henry} foods.")

elif food_eaten_by_henry:
    if food_eaten_by_henry == 1:
        print(f"Henry ate: {food_eaten_by_henry} food.")

    else:
        print(f"Henry ate: {food_eaten_by_henry} foods.")

else:
    print("Henry remained hungry. He will try next weekend again.")
