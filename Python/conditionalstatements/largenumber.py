# Program which takes two numbers from the user and prints below output:-
#num1 is greater than num2 if num1 is greater than num2
#num1 is smaller than num2 if num1 is smaller than num2
#num1 is equal to num2 if num1 and num2 are equal
#Note: -
# 1. Do this problem using if - else
# 2. Do this using ternary operator
##1.
n1,n2 = input('Enter two numbers: ').split(' ')
n1, n2 = float(n1), float(n2)
if n1 > n2 :
    print("{} is greater than {}".format(n1,n2))
elif n1 < n2:
    print("{} is greater than {}".format(n2,n1))
else:
    print("{} is equal to {}".format(n1,n2))
##2.
"{} is greater than {}".format(n1,n2) if n1 > n2 else "{} is greater than {}".format(n2,n1)
