# program to read input from user. Allow the user to enter more numbers as
# long as the user enters valid integers. Terminate the program with
# proper message when they entered value is anything except integer.
while(True):
    n = input('Enter an integer: ') # read input from the user
    FLAG = False # create a flag to track the number validation
# validate your number
    if(n.isdigit()): # is.digit() returns True only when n is an integer
        FLAG = True
    else:
        FLAG = False
    if(FLAG== True): # When number 'n' is an integer go to back of the while loop
        pass # pass is a keyword that works similar to continue; continue works only wit
    else:
        print('Invalid input')
        break # when break keyword is hit, loop will exit.
