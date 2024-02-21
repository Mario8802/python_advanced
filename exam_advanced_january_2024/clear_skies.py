import math
import sys

size_of_the_protected_airspace = int(input())

Su_27 = 4 #This is the closest Soviet plane similar to the F-14
initial_armor_value = 300

the_rows_of_the_airspace = []
aircraft_position = []


for current_row in range(size_of_the_protected_airspace):
    airspace = list(input())
    the_rows_of_the_airspace.append(airspace)

    if 'J' in airspace:
        current_column = airspace.index('J')
        aircraft_position = [current_row, current_column]
        the_rows_of_the_airspace[current_row][current_column] = '-'

F14_directions = {
    'left': (0, -1),
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
}

while initial_armor_value > 0 and Su_27:
    direction = input()

    row_pos, col_pos = (aircraft_position[0] + F14_directions[direction][0],
                        aircraft_position[1] + F14_directions[direction][1])

    symbol = the_rows_of_the_airspace[row_pos][col_pos]

    the_rows_of_the_airspace[row_pos][col_pos] = '-'

    aircraft_position = [row_pos, col_pos]

    if symbol == 'E':
        Su_27 -= 1

        if Su_27:
            initial_armor_value -= 100

    elif symbol == 'R':
        initial_armor_value = 300

the_rows_of_the_airspace[aircraft_position[0]][aircraft_position[1]] = 'J'

if not Su_27:
    print("Mission accomplished, you neutralized the aerial threat!")

elif not initial_armor_value:
    print(f'Mission failed, your jetfighter was shot down!'
          f' Last coordinates [{aircraft_position[0]}, {aircraft_position[1]}]!')

[print(*r, sep='') for r in the_rows_of_the_airspace]



# 02. Clear Skies
#
# A jetfighter surveys the surrounding area for enemy aircraft.
# You will be given an integer n for the size of the protected airspace (square-shaped matrix). On the next n lines,
# you will receive the rows of the airspace.
# The jetfighter will start at a random position, marked with the letter 'J'. In random positions also, enemy aircraft
# will be marked with the letter 'E'. There will also be repair points marked with the letter 'R'. All of the empty
# positions will be marked with the symbol'-'.
# The jetfighter has an initial armor value of 300 units. When it receives a command, it moves one position towards
# the given direction.
# The program will end when аll enemy planes are shot down or the jetfighter’s armor becomes 0. The final state of
# the airspace must always be printed on the console at the end.
# On each turn, you will be guiding the jetfighter and giving it the direction, to move towards. The commands will
# be "up", "down", "left" and "right".
#     • If a position with '-' (dash) is reached, it means that the field is empty and the jetfighter awaits its
#     next direction.
#     • If it encounters an enemy aircraft marked with 'E', a battle begins:
#     • The jetfighter shoots down the enemy plane (the position of the destroyed enemy plane will be marked with '-'
#     (dash)
#     • In case this is the last enemy, the program ends and the following message should be displayed on the console:
#     "Mission accomplished, you neutralized the aerial threat!"
#         ◦ Do not forget the final state of the airspace.
#     • In case this is not the last enemy, the jetfighter takes damage – its armor loses 100 units.
#         ◦ If its armor reaches zero, it crashes and the mission fails. The program ends and the following message
#         should be displayed on the console: "Mission failed, your jetfighter was shot down!
#         Last coordinates [{row}, {col}]!"
#         ◦ Do not forget the final state of the airspace.
#     • If a position marked with 'R' is reached your plane is repaired and restores its armor to 300 units.
#         ◦ The position must be marked with '-' (dash).
# Input
#     • On the first line, you are given the integer n – the size of the matrix (airspace).
#     • The next n lines hold the values for every row.
#     • On each of the next lines, you will get a direction command.
# Output
#     • If all enemy planes are shot down, print:
#     • "Mission accomplished, you neutralized the aerial threat!"
#     • If your jetfighter is hit by an enemy plane three times, print:
#     • "Mission failed, your jetfighter was shot down! Last coordinates [{row}, {col}]!".
#     • At the end, print the final state of the matrix (airspace) with the last known position
#     of your jetfighter on it.
# Constraints
#     • The size of the square matrix (airspace) will be between [4…10].
#     • The jetfighter starting position will always be marked with 'J'.
#     • There will be always four enemy aircraft - fields marked with 'E'.
#     • There will be always a random count (1…5) fields marked with 'R' (repair).
#     • The commands given will direct the jetfighter only within the limits of the matrix (airspace).
#     • There will be always two output scenarios - either the enemy shoots down your plane or your plane
#     shoots down all the enemy planes.
#     • You will always receive enough commands to end the battle.