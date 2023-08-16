# 1. Python Program to Count the Number of Vowels Present in a String using Sets:
s=input("Enter string:")
count = 0
vowels = set("aeiou")
for letter in s:
if letter in vowels:
count += 1
print("Count of the vowels = {}".format(count))
