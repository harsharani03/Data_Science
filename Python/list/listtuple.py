# Create a List of Tuples with the First Element as the Number and Second
# Element as the Square of the Number:
list_of_tuples = []
for item in range(1,11):
    list_of_tuples.append((item, item**2))
print('List of tuples for integers 1:10 = {}'.format(list_of_tuples))
