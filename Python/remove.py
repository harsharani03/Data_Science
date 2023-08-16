# 3. Program to Remove the Given Key from a Dictionary:
## let's assume a dictionary
d = {"name":["A","B","C"],
"scores":[80,40,50],
"Age":[34,22,23]}
# let's assume key
# key = 'val'
key = 'name'
print('before removal: {}'.format(d))
d.pop('name')
print('after removal: {}'.format(d))
