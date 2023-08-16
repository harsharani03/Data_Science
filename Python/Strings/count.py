str="Hi! I am 5 years old, my favorite number is 0 "
digit_count=0
letter_count=0
special_count=0
for i in str:
    if i in '0123456789':
        digit_count=digit_count+1
    elif i.lower() in 'abcdefghijklmn0pqrstuvwxyz':
        letter_count=letter_count+1
    else:
        special_count=special_count+1
print("{} has {} digits , {} letters and {} special characters".format(str,digit_count,letter_count,special_count))
