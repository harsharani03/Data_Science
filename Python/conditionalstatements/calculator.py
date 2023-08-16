# Please select any one operation from below:-
# 1. To add enter 1
# 2. to subtract enter 2
# 3. To multiply enter 3
# 4. To divide enter 4
# 5. To divide and find quotient enter 5
# 6. To divide and find remainder enter 6
# 7. To find num1 to the power of num2 enter 7
# 8. To Come out of the program enter 8
while True:
    n1, n2 = [int(i) for i in input('Enter two integers: ').split(' ')]
    print('''1. To add enter 1
    2. to subtract enter 2
    3. To multiply enter 3
    4. To divide enter 4
    5. To divide and find quotient enter 5
    6. To divide and find remainder enter 6
    7. To find num1 to the power of num2 enter 7
    8. To Come out of the program enter 8''')
    op = int(input())
##
    if op == 1:
        print(n1+n2)
    elif op == 2:
        print(n1 - n2)
    elif op == 3:
        print(n1*n2)
    elif op == 4:
        if n2!= 0:
            print(n1/n2)
        else:
            print('Error: division by zero invalid')
    elif op == 5:
        if n2!= 0:
            print(n1//n2)
        else:
            print('Error: division by zero invalid')
    elif op == 6:
        if n2!= 0:
            print(n1%n2)
        else:
            print('Error: division by zero invalid')
    elif op == 7:
        print(n1**n2)
    else :
        break
