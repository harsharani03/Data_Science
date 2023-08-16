# Define a Sum Function which accepts variable number of integers as an arguments.
# function defination
def sum_val(*arg):
    return sum(arg)

# function call
print(sum_val(3,4,5))
print(sum_val())
print(sum_val(3,4,5,20))
