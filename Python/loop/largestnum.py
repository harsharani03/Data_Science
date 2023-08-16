# Program to Find the Largest Number in a List:
### assuming list of numeric types
print('Largest Number in the list {} = {}'.format([30,20,10,45,10], max([30,20,10,45,10])))
print('Largest Number in the list {} = {}'.format([30,200,10,45,10], max([30,200,10,45,1])))
## using loop
mylist = [30,20,10,45,10]
## assume 1st element as maximum value
max_ele = mylist[0]
for item in mylist:
    if item > max_ele:
        max_ele = item
print('Largest Number in the list {} = {}'.format(mylist, max_ele))
