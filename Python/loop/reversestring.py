# python program to find below output using loop:-
#Input: - 'peter piper picked a peck of pickled peppers.'
#Output:- 'peppers pickled of peck a picked piper peter'
mystr = 'peter piper picked a peck of pickled peppers.'
print('Input:- {}'.format(mystr))
## using loop
## replacing '.'
mystr = mystr[:len(mystr) - 1]
i = len(mystr) - 1
last_indx = len(mystr)
newstr = []
while i >= 0:
    if mystr[i] == ' ':
        newstr.append(mystr[i+1 : last_indx ])
        last_indx = i
    elif i == 0:
        newstr.append(mystr[i : last_indx ])
    i = i - 1
print('Method 1: Output:- {}'.format(" ".join(newstr)))
## using inbuilt method
print('Method 2: Output:- {}'.format(" ".join(mystr.split(' ')[::-1])))
