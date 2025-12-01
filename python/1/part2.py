# Doesn't work

arrow = 50
password = 0
password2 = 0
rotations = []

def move_arrow(arrow, direction, n) -> tuple:

    new_arrow = (arrow + (n if direction == 'right' else -n)) # left is negative, right is positive

    wrapped_new_arrow = new_arrow % 100

    # This is to see if and how many loops the arrow does
    if direction == 'right':
        passed_zero = (arrow + n >= 100) # Bool
    elif direction == 'left':
        passed_zero = (arrow - n < 0) # Bool

    if passed_zero:
        loops = abs(new_arrow // 100)
    else:
        loops = 0
    
    # what if it starts on 0 ? what if it ends on 0 ?

    #debugging print
    print(f'arrow={arrow}, new arrow={wrapped_new_arrow}, direction = {direction}, steps = {n}, passed_z = {passed_zero}, loops: {loops}')

    return wrapped_new_arrow, passed_zero, loops

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

    print(new_arrow)

    if new_arrow[0] == 0:
        password += 1
        password2 += 1
    
    if new_arrow[1] == True: #Passed zero
        password2 += 1*new_arrow[2]

    print("\nPart 1 PASSWORD:", password)
    print("Part 2 PASSWORD:", password2)

    arrow = new_arrow[0]

print("\nPart 1 PASSWORD:", password)
print("Part 2 PASSWORD:", password2)