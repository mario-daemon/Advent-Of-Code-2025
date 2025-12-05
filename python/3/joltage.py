import time
start = time.perf_counter()

joltages = []

def find_largest_nums(bank) -> tuple:
    first_largest = 0

    for num in bank[:-1]:
        num = int(num)
        if num > first_largest:
            first_largest = num

    first_largest_pos = bank.find(str(first_largest))
    cut_bank = bank[first_largest_pos+1:]

    second_largest = 0

    for num in cut_bank:
        num = int(num)
        if num > second_largest:
            second_largest = num

    return first_largest, second_largest

def make_into_joltage(b1, b2) -> int:
    combined_digits = str(b1) + str(b2)
    return int(combined_digits)

with open('batteries.txt','r') as file:
    for bank in file:

        batteries = find_largest_nums(bank.strip())
        joltage = make_into_joltage(*batteries)
        joltages.append(joltage)

total_joltage = sum(i for i in joltages)
print(total_joltage)

end = time.perf_counter()
print(f'Execution time: {end - start:.8f} seconds')