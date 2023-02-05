def longestCommonPrefix(strs) -> str:
    prefix = ""
    shortest = min(strs, key=len)
    strs.remove(shortest)                       # Slows things down; not necessary
    
    word = dict(enumerate(shortest))            # Don't need the dictionary; we can just work based on the shortest with enumerate()

    for i in range(len(shortest)):
        for j in strs:
            if j[i] != word[i]:
                return prefix                   # We can return up until the index instead
            
        prefix += word[i]
    return prefix

def longestCommonPrefixEfficient(strs) -> str:
    shortest = min(strs, key=len)

    for i, letter in enumerate(shortest):
        for j in strs:
            if j[i] != letter:
                return shortest[:i]

    return shortest

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["doc","racecar","car"]))

print(longestCommonPrefixEfficient(["flower","flow","flight"]))
print(longestCommonPrefixEfficient(["doc","racecar","car"]))