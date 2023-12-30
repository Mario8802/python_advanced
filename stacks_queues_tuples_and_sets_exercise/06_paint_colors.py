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