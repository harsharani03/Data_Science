# python program to find below output using loop:-
#Input:- 'This is Python class', sep = 'is',
#Output:- ['This', 'Python class']
mystr = 'This is Python class'
sep = 'is'
print('Input:- {}'.format(mystr))
## using loop
outlist = []
for each in mystr.split(' '):
    if each != sep:
        outlist.append(each)
print('Output:- {}'.format(outlist))
