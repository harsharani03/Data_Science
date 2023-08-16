# Python program to iterate over dictionaries using for loops:
## let's assume a dictionary
d = {"name":["A","B","C"],
"scores":[80,40,50],
"Age":[34,22,23]}
## getting both keys & values
for k,v in d.items():
    print(k,v)
## getting keys
for k in d.keys():
    print(k)
## getting values
for v in d.values():
    print(v)
