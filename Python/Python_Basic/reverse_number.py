num=123456789
reverse_num=0

while num!=0:
    digit=num%10
    reverse_num=reverse_num*10+digit
    num//=10
    
print("Reversed Number:{}".format(reverse_num))
