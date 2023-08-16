# Python program to find the total number of times letter 'p' is
# appeared in the below string using loop:-
my_str = 'peter piper picked a peck of pickled peppers.\n'
## 1. using inbuilt
print('Count of \'p\' in string - {} = {}'.format(my_str, my_str.count('p')))
## 2. using loop
counter = 0
for char in my_str:
    if char == 'p':
        counter += 1
print('Count of \'p\' in string - {} = {}'.format(my_str, counter))
