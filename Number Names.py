unique = {    0   : "zero", 
                    1   : "one", 
                    2   : "two", 
                    3   : "three", 
                    4   : "four", 
                    5   : "five", 
                    6   : "six", 
                    7   : "seven", 
                    8   : "eight", 
                    9   : "nine",
                    10  : "ten",
                    11  : "eleven", 
                    12  : "twelve",
                    13  : "thirteen",
                    14  : "fourteen",
                    15  : "fifteen",
                    16  : "sixteen",
                    17  : "seventeen",
                    18  : "eighteen",
                    19  : "nineteen",
                    20  : "twenty",
                    30  : "thirty",
                    40  : "forty",
                    50  : "fifty",
                    60  : "sixty",
                    70  : "seventy",
                    80  : "eighty",
                    90  : "ninety"
                }

powers = {  100             :   "hundred",
            1000            :   "thousand",
            1000000         :   "million",
            1000000000      :   "billion",
            1000000000000   :   "trillion"
        }

def compound(number):
    modulo = number % 10
    number //= 10
    number *= 10
    return unique.get(number) + "-" + unique.get(modulo)

def hundreds(number):
    string = unique.get(number // 100) + " " + powers.get(100)
    modulo = number % 100

    if modulo == 0:
        return string
    elif modulo in unique:
        return string + " " + unique.get(modulo)
    elif modulo < 100:
        return string + " " + compound(modulo)

def number_name(number):
    # Returns the uniquely named numbers (i.e "one," "ten," "eleven," "nineteen," "ninety")
    if number in unique:
        return unique.get(number)

    upper_range = 1000

    # Returns the name from 1-999
    if number < upper_range:
        if number in unique:
            if number == 0:
                return ""
            else:
                return unique.get(number)
        elif number < 100:
            return compound(number)
        else:
            return hundreds(number)

    while upper_range < number:
        lower_range = upper_range
        upper_range *= 1000

    # Returns the name within the range
    return number_name(number // lower_range) + " " + powers.get(lower_range) + " " + number_name(number % lower_range)

while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break

    if list(powers.keys())[list(powers.values()).index("trillion")] * 1000 < number:
        print("Please enter a number below quadrillion: ")
        continue

    print(number_name(number))

print("Closing the program...")
print("Goodbye!")