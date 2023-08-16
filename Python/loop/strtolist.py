# Python program to find below output using loop:-
mystr = 'peter piper picked a peck of pickled peppers.'
print('Input:- {}'.format(mystr))
## using loop
i = 0
from_indx = 0
str_list = []
while i < len(mystr):
    if mystr[i] == ' ':
        curr_indx = i
        str_list.append(mystr[from_indx:curr_indx])
        from_indx = i+1
    elif i == len(mystr) - 1:
        str_list.append(mystr[from_indx:])
    i += 1
print('Method 1: Output:- {}'.format(str_list))
## using inbuilt method
print('Method 2: Output:- {}'.format(mystr.split(' ')))
