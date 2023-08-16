# Program to Check if a Given Key Exists in a Dictionary or Not:
## let's assume a dictionary
d = {"name":["A","B","C"],
"scores":[80,40,50],
"Age":[34,22,23]}
# let's assume key
# key = 'val'
key = 'name'
## let's find out if a key exists or not as keys on the given dictionary
flag = False
for k in d.keys():
    if k == key:
        print('Key Found!!')
        flag = True
        break
if flag == False:
    print('Key Not Found!!')
