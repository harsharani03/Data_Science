# Program to check if this tuple (20, 20, 30, 30, 30, 40, 40, 40, 10) is in
# ascending/ descending or in random order without inbuilt function.
# t = (20, 20, 30, 30, 30, 40, 40, 40, 10)
# t = (20, 20, 30, 30, 30, 40, 40, 40)
t = (40, 40, 30,20,10)
## generate flags
i = 0
flag = False
isasc, isdes = False, False
while i <len(t) - 1:
    if t[i] >= t[i+1]:
        isasc = True
    else:
        isasc = False
        break
i += 1
i = 0
while i <len(t) - 1:
    if t[i] <= t[i+1]:
        isdes = True
    else:
        isdes = False
i += 1
if isasc:
    print('Ascending Order')
elif isdes:
    print('Ascending Order')
else:
    print('Random Order')
