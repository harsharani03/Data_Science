# 12. Write a python program to find below output using loop:-
mystr = 'peter piper picked a peck of pickled peppers.'
print('Input:- {}'.format(mystr))
## using loop
i = len(mystr) - 1
newstr = ''
while i >= 0:
    newstr = newstr + mystr[i]
    i = i -1
print('Method 1: Output:- {}'.format(newstr))
## using inbuilt method
print('Method 2: Output:- {}'.format(mystr[::-1]))
