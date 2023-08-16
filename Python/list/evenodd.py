# Program to Put Even and Odd elements in a List into Two Different Lists:
even = []
odd = []
for item in range(0,20): # assuming list of values 0 to 19
    if item%2 == 0:
        even.append(item)
    else:
        odd.append(item)
print('Even List: {}'.format(even))
print('Odd List: {}'.format(odd))
