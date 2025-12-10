import time
start_time = time.perf_counter()


text = []
with open('input.txt','r') as f:
    for line in f:
        text.append(line.strip())

counter = 0

for idx, line in enumerate(text):

    is_top_line = (line == text[0])
    is_bottom_line = (line == text[-1])

    for id, char in enumerate(line):

        if char == '.':
            continue
        else:

            is_first_char =(id == 0)
            is_last_char =(id == len(line)-1)

            if is_top_line:   
                tp = False

            if is_bottom_line:
                btm = False
                
            if is_first_char:
                lf = False
            
            if is_last_char:
                rt = False
            

            left = line[id-1] if not is_first_char else None
            right = line[id+1] if not is_last_char else None
            top = text[idx-1][id] if not is_top_line else None
            bottom = text[idx+1][id] if not is_bottom_line else None
            top_left = text[idx - 1][id - 1] if not is_top_line and not is_first_char else None
            top_right = text[idx - 1][id + 1] if not is_top_line and not is_last_char else None
            bottom_left = text[idx + 1][id - 1] if not is_bottom_line and not is_first_char else None
            bottom_right = text[idx + 1][id + 1] if not is_bottom_line and not is_last_char else None

            pos_of_interest = [left, right, top, bottom, top_left, top_right, bottom_left, bottom_right]

            valid_neighbours = []

            for i in pos_of_interest:
                if i == '@':
                    valid_neighbours.append(i)
            '''
            print("----")
            print("l", idx, "p", id)
            print(valid_neighbours)
            print("----")
            #print(len(valid_neighbours))
            '''
            if len(valid_neighbours) < 4:
                counter += 1


print(counter)
end_time = time.perf_counter()
print(f'Execution time: {end_time - start_time:.8f} seconds')