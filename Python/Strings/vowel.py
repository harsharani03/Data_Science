string="Apple"
vowel_count=0
for i in string:
    if i.lower() in 'aeiou':
        vowel_count=vowel_count+1
print("number of vowels in {} is:{}".format(string,vowel_count))
