# Program to Read a List of Words and Return the Length of the Longest One:
words = input('Enter many words seperated by comma: ').split(' ')
## initalizing with first elements value
max_len = len(words[0])
max_word = words[0]
for member in words:
    if len(member) > max_len:
        max_len = len(member)
        max_word = member
print('Length of longest word ({}) = {}'.format(max_word, max_len))
