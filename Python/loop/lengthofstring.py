# Python program to find the length of the my_str using loop
my_str = "find length of a string"
## 1. using builtin function
print('Method 1: Length of string - {} = {}'.format(my_str, len(my_str)))
## 2. using loop
counter = 0
while counter < len(my_str):
    counter += 1
print('Method 2: Length of string - {} = {}'.format(my_str, counter))
