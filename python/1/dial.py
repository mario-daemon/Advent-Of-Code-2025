# Part 1 done in 1h 18m

arrow = 50
password = 0
rotations = []

def move_arrow(arrow, direction, n) -> tuple:

    new_arrow = (arrow + (n if direction == 'right' else -n)) # left is negative, right is positive

    wrapped_new_arrow = new_arrow % 100

    #debugging print
    #print(f'arrow={arrow}, new arrow={wrapped_new_arrow}, direction = {direction}, steps = {n}')

    return wrapped_new_arrow

with open("rotations.txt", "r") as file:
    for line in file:
        line = line.strip()
        rotations.append(line)

for rotation in rotations:

    n_clicks = int(rotation[1:])

    if rotation[0] == 'L':
        new_arrow = move_arrow(arrow, 'left', n_clicks)

    elif rotation[0] == 'R':
        new_arrow = move_arrow(arrow, 'right', n_clicks)

    if new_arrow == 0:
        password += 1

    arrow = new_arrow

print("\nPart 1 PASSWORD:", password)