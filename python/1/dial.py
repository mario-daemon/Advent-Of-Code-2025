# Done in 1h 18m

arrow = 50
password = 0
rotations = []

def move_arrow(arrow, direction, n):

    new_arrow = arrow + (n if direction == 'right' else -n) # right is positive, left is negative

    print(f'arrow={arrow}, new arrow={new_arrow}, direction = {direction}, steps = {n}') #debugging

    # To make sure the arrow loops back and stays between 0 and 99:

    hundreds_place = 1

    if new_arrow < 0:
        hundreds_place = new_arrow // -100
    elif new_arrow > 100:
        hundreds_place = new_arrow // 100

    if new_arrow >= 100:
        return new_arrow - (100*hundreds_place)
    elif new_arrow < 0:
        return new_arrow + (100*hundreds_place)
    else:
        return new_arrow

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

print("\nPASSWORD:", password)