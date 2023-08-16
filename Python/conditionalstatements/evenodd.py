# 4. W A P which takes one number from the user and checks whether it is
# an even or odd number? If it even then prints number is even number
# else prints that number is odd number.
n = int(input('Enter an integer: '))
if n%2 == 0:
    print('{} is an even number.'.format(n))
else:
    print('{} is an odd number.'.format(n))
