# 1. WAP to add elements of the two lists:
# List1 = [6,9,7,5,10]
# List2 = [10,20,30,50,7]

## method 1:
added_ele = []
List1 = [6,9,7,5,10]
List2 = [10,20,30,50,7]

for e1,e2 in zip(List1, List2):
    added_ele.append(e1+e2)
print('List after element-wise addition: {}'.format(added_ele))
## method 2:
added_ele = [e1+e2 for e1,e2 in zip(List1, List2)]
print('List after element-wise addition: {}'.format(added_ele))
