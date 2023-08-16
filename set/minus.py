# Python Program that displays which Letters are in the First String but not in the S
s1 = "abc strings"
s2 = "str"
print('Letters present only in first string are {}'.format(set(s1) - (set(s2))))
