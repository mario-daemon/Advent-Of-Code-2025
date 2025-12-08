# This one was very easy, but my execution time is not as optimal as other exercises

import time
start = time.perf_counter()

list = []

def get_invalid_ids(min: int, max: int):

    min = int(min)
    max = int(max)

    rrange = range(min,max+1)
    for i in rrange:

        i = str(i)

        if len(i) % 2 != 0: # if the number is odd in length, discard
            continue
        else:
            half = int(len(i)/2)

            if i[:half] == i[half:]: # if the first half is equal to the second half
                list.append(i)


with open('ranges.txt','r') as file:
    text = file.read()

sets = text.split(',')

for i in sets:
    min, max = i.split('-')
    get_invalid_ids(min,max)

answer = sum(int(x) for x in list)
print(answer)

end = time.perf_counter()
print(f'Execution time: {end - start:.8f} seconds')