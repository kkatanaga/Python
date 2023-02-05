def factorial_iterate(n):
    if n == 0:
        return 1
    
    output = n
    while n-1 > 0:
        n -= 1
        output *= n
    
    return output

def factorial_recurse(n):
    if n == 0:
        return 1
    
    return n * factorial_recurse(n-1)

prompt_message = "Enter a number: "
number = int(input(prompt_message))
iterate = factorial_iterate(number)
recurse = factorial_recurse(number)
print(f"Number: {number}")
print(f"Iterate: {iterate}")
print(f"Recurse: {recurse}")