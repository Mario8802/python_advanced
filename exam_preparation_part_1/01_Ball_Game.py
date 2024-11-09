from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())

scored_goals = 0

while strength and accuracy:
    last_strength = strength[-1]
    first_accuracy = accuracy[0]

    if last_strength + first_accuracy == 100:
        strength.pop()
        accuracy.popleft()
        scored_goals += 1
    elif last_strength + first_accuracy < 100:
        if last_strength < first_accuracy:
            strength.pop()
        elif last_strength > first_accuracy:
            accuracy.popleft()
        else:  
            strength[-1] += first_accuracy
            accuracy.popleft()
    else:  
        strength[-1] -= 10
        accuracy.append(accuracy.popleft())

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
else:  
    print("Paul failed to make a hat-trick.")

if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")

if strength:
    print(f"Strength values left: {', '.join(map(str, strength))}")
if accuracy:
    print(f"Accuracy values left: {', '.join(map(str, accuracy))}")
# SPAGHETTI

