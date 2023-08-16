# python program to implement replace method using loop. If
# sub_str is found in my_str then it will replace the first occurrence of
# sub_str with new_str else it will will print sub_str not found:-
#Input: - my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
#sub_str = 'Peck', new_str = 'Pack'
#Output: - 'Peter Piper Picked A Pack Of Pickled Peppers.'
mystr = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'
print('Input:- {}'.format(mystr))
curr_indx = 0 # a pointer to current character
from_indx = 0 # a pointer to hold start of a sub-string
newstr = ''
IS_FOUND = False # to track first occurrence of sub_str
while curr_indx < len(mystr):
    if mystr[curr_indx] == ' ':
        if sub_str == mystr[from_indx:curr_indx]:
            newstr = newstr + new_str + mystr[curr_indx:]
            IS_FOUND = True
            break
    elif curr_indx == len(mystr) - 1:
        if sub_str == mystr[from_indx:curr_indx]:
            newstr = newstr + new_str + mystr[curr_indx:]
            IS_FOUND = True
            break
    curr_indx += 1
if IS_FOUND == False:
    print('Output:- {} not found.'.format(sub_str))
else:
    print('Output:- {}'.format(newstr))
