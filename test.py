roman_numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "t":0}

def romanToInt(s: str) -> int:
    if len(s) == 1:
        return roman_numerals[s]
    
    roman = list(s + "t")
    left = int(roman_numerals[roman[0]])
    
    sum = left
    for letter in roman[1:]:
        if left < roman_numerals[letter]:
            sum += abs((2 * left) - roman_numerals[letter])
        else:
            sum += roman_numerals[letter]
        left = int(roman_numerals[letter])
    return sum
    
print(romanToInt("LVIII"))