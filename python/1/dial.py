# Took me way too long to be honest

arrow = 50
password = 0
password2 = 0
rotations = []

def move_arrow(arrow, direction, n) -> tuple:

    new_arrow = (arrow + (n if direction == 'right' else -n)) # left is negative, right is positive


    full_loops = abs(n) // 100
    remainder = abs(n) % 100

    if direction == 'right':
        first_loop_at = 100 - arrow
    elif direction == 'left':
        if arrow == 0:
            first_loop_at = 100 # Otherwise starting from 0 and going left will count as a loop
        else:
            first_loop_at = arrow

    if remainder > first_loop_at:
        one_more_loop = 1
    else:
        one_more_loop = 0

    loops = full_loops + one_more_loop
    passed_zero = loops > 0 # Bool

    wrapped_new_arrow = new_arrow % 100

    #debugging print
    #print(f'arrow={arrow}, direction = {direction}, steps = {n}, new arrow={wrapped_new_arrow}, passed_z = {passed_zero}, loops: {loops}')

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

    if new_arrow[0] == 0:
        password += 1
        password2 += 1
    
    if new_arrow[1] == True: #Passed zero
        password2 += 1*new_arrow[2]
        pass
    
    #print("Part 1 PASSWORD:", password) #debugging
    #print("Part 2 PASSWORD:", password2) #debugging

    arrow = new_arrow[0]

print("Part 1 PASSWORD:", password)
print("Part 2 PASSWORD:", password2)