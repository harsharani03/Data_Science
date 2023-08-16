Str="Hello! How are you?"
new_str=''
for i in range(1,len(Str)+1):
    new_str=new_str+(Str[-i])
print(new_str)
