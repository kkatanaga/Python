with open("day1_input.txt") as f:
    calories = 0
    largest = 0
    new_line = ''

    for line in f:
        if line == '\n':
            largest = max(largest, calories)
            calories = 0

        else:
            new_line = line.replace("\n", "")
            calories += int(new_line)

largest = max(largest, calories)
print(largest)
f.close()

with open("day1_input.txt") as f:
    calories = 0
    first, second, third = 0, 0, 0
    new_line = ''

    for line in f:
        if line == '\n':
            if third < calories:
                if second < calories:
                    third = second
                    if first < calories:
                        second = first
                        first = calories
                    else:
                        second = calories
                else:
                    third = calories

            calories = 0

        else:
            new_line = line.replace("\n", "")
            calories += int(new_line)

first = max(first, calories)
print(f"first: {first}")
print(f"second: {second}")
print(f"third: {third}")
print(f"sum: {first + second + third}")

f.close()
