Str="noon"
new_str=''
for i in range(1,len(Str)+1):
    new_str=new_str+(Str[-i])
if Str==new_str:
    print("{} is palindrome".format(Str))
else:
    print("{} is not palindrome".format(Str))
