# python program to implement index method using loop. If
# sub_str is found in my_str then it will print the index of first occurrence
# of first character of matching string in my_str:-
mystr = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
print('Input:- {}'.format(mystr))
i = 0
from_indx = 0
newstr = ''
while i < len(mystr):
    if sub_str == mystr[i:i+len(sub_str)]:
# return index of first character
# print(i)
        break
    i += 1
print('Output:- {}'.format(i))
