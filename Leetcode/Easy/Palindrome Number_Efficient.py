def isPalindrome(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False

    result = 0
    while x > result:
        result = (result * 10) + (x % 10)
        x //= 10
    
    return True if (x == result or x == result // 10) else False

print(isPalindrome(111))