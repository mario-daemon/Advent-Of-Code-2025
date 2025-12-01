# 13:25

arrow = 50
password = 0
rotations = []

def move_left(arrow, n):
    return arrow - n
    
def move_right(arrow, n):
    return arrow + n

with open("rotations.txt", "r") as file:
    for line in file:
        line = line.strip()
        rotations.append(line)

for rotation in rotations:

    n_clicks = int(rotation[1:])

    if rotation[0] == 'L':
        new_arrow = move_left(arrow, n_clicks)

    elif rotation[0] == 'R':
        new_arrow = move_right(arrow, n_clicks)

    if (new_arrow%50 == 0) or (new_arrow == 0):
        password += 1

    arrow = new_arrow

print(arrow)