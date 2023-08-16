# 1. W. A P. which takes one number from 0 to 9 from the user and prints it
# in the word. And if the word is not from 0 to 9 then it should print that
# number is outside of the range and program should exit.
#
digit = input('Enter a number : ')
if digit.isdigit() == False:
    print('Error: invalid input type')
else:
    if (int(digit) > 9) | (int(digit) < 0):
        print('Number is outside range')
    else:
        word_list = []
        for each in list(digit):
            if each == '1':
                word_list.append('one')
            elif each == '2':
                word_list.append('two')
            elif each == '3':
                word_list.append('three')
            elif each == '4':
                word_list.append('four')
            elif each == '5':
                word_list.append('five')
            elif each == '6':
                word_list.append('six')
            elif each == '7':
                word_list.append('seven')
            elif each == '8':
                word_list.append('eight')
            elif each == '9':
                word_list.append('nine')
            else:
                word_list.append('zero')
        print('Word for of number {} = {}'.format(digit, " ".join(word_list)))
