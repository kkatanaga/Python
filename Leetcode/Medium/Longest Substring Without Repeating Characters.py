def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    substrings = list(s[0])
    index = 0
    for i in range(1, len(s)):
        for j in s[i:]:
            if j in substrings[index]:
                substrings.append(s[i])
                index += 1
                break
            substrings[index] += j
    
    max = 0
    for i in substrings:
        length = len(i)
        if max < length:
            max = length
    
    return max

print(lengthOfLongestSubstring("dvdf"))