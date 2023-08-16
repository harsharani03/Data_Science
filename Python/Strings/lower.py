str="Hi! I am 5 years old, my favorite number is 0 "
lower_count=0
for i in str:
    if i in 'abcdefghijklmn0pqrstuvwxyz':
        lower_count=lower_count+1
print("{} has {} lower case characters".format(str,lower_count))
