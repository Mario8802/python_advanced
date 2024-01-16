from collections import deque
colors_string = deque(input().split())

main_colors = ['red', 'blue', 'yellow']
secondary_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['blue', 'yellow'],
}
collected_colors = []
while colors_string:
    first_string = colors_string.popleft()
    last_string = colors_string.pop() if colors_string else ''
    if first_string + last_string in main_colors or first_string + last_string in secondary_colors:
        collected_colors.append(first_string + last_string)
    elif last_string + first_string in main_colors or last_string + first_string in secondary_colors:
        collected_colors.append(last_string + first_string)
    else:
        if len(first_string) > 1:
            colors_string.insert(len(colors_string) // 2, first_string[:-1])
        if len(last_string) > 1:
            colors_string.insert(len(colors_string) // 2, last_string[:-1])
for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break
print(collected_colors)

------------------------------------------------------------------------------------------
from collections import deque

words = deque(input().split())  # d yel blu e low redd

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):  # 'd' 'redd' -> '', 'red'
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)

print(result)
