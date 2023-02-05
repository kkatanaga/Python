def isPalindrome(x):
    if x < 0:
        return False

    left = 0
    right = 0
    
    power = 1
    while True:
        if power * 10 > x:
            break
        power *= 10

    while 0 <= x:
        if x == 0:
            return True

        left = x // power
        right = x % 10

        if left != right:
            return False

        x %= power
        x = int(x / 10)
        power /= 100

        if power == 1:
            return True

print(isPalindrome(10))