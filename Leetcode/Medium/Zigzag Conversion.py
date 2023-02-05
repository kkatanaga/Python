def alternatingSlice(line, length, start, firstAdd, secondAdd):
    stringSlice = line[start]
    index = start + firstAdd

    while index < length:
        stringSlice += line[index]

        index += secondAdd
        if index >= length:
            break

        stringSlice += line[index]

        index += firstAdd
    
    return stringSlice

def convert(s, numRows) -> str:
    sLength = len(s)
        
    if sLength < numRows or numRows < 2:
        return s

    maxIndex = numRows - 1
    newS = ""
    for i in range(numRows):
        firstSum = (2 * (maxIndex)) - i
        firstAddend = firstSum - i
        secondSum = (2 * (maxIndex)) + i
        secondAddend = secondSum - firstSum
        if firstAddend == 0:
            firstAddend = secondAddend
        elif secondAddend == 0:
            secondAddend = firstAddend
            
        newS += alternatingSlice(s, sLength, i, firstAddend, secondAddend)
    
    return newS

print(alternatingSlice("PAYPALISHIRING", 14, 0, 6, 6))
print(alternatingSlice("PAYPALISHIRING", 14, 1, 4, 2))
print(alternatingSlice("PAYPALISHIRING", 14, 2, 2, 4))
print(alternatingSlice("PAYPALISHIRING", 14, 3, 6, 6))
print(convert("PAYPALISHIRING", 4))
print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 2))
print(convert("AB", 1))
            