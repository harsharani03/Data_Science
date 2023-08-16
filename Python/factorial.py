# WAF to find factorial of a positive number. Return -1 if input to the function is a
# - Using for loop
# - Using while loop

### function defination
def factorial(n):
    if (n == 0) | (n == 1):
        return 1
    elif n > 1:
        f = 1
        while n > 1:
            f *= n
            n -= 1
            return f
    else:
        return -1 # invalid inputs
## function call
print(factorial(0))
print(factorial(-1))
print(factorial(1))
print(factorial(5))
## using while loop

print(factorial(4))
