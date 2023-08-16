# 15.WAF to return appropriate message as follows:
# If the sequence is in ascending order: return “Ascending order”
# If the sequence is in descending order: return “Descending order”
# Else: “Random order”
# Test case sequences:
# (10,10,20,30,20,20)
# (20,20,30,30,30,40,40,40)
# (20,20,30,30,30,29,40,40,40)
# (20,20,30,30,30,40,40,40,10)
# (20,20,20,30,30,30,40,40,40)
# (20,20,30,30,30,40,40,40,31)
# (40,40,40,30,20,20,20)
# (40,40,40,30,20,20,20,10)
# (40,40,40,30,10,20,20)
def find_sequence_order(t):
    i = 0
    flag = False
    isasc, isdes = False, False
    unsorted_t = t
    if sorted(t) == list(unsorted_t):
        isasc = True
    elif sorted(t, reverse = True) == list(unsorted_t):
        isdes = True
    else:
        isdes = False
        isasc = False
    
    if isasc:
        return '{} is in Ascending Order'.format(t)
    elif isdes:
        return '{} is in Descending Order'.format(t)
    else:
        return '{} is in Random Order'.format(t)
    
### function call
print(find_sequence_order((10,10,20,30,20,20)))
print(find_sequence_order((20,20,30,30,30,40,40,40)))
print(find_sequence_order((20,20,30,30,30,29,40,40,40)))
print(find_sequence_order((20,20,30,30,30,40,40,40,10)))
print(find_sequence_order((20,20,20,30,30,30,40,40,40)))
print(find_sequence_order((20,20,30,30,30,40,40,40,31)))
print(find_sequence_order((40,40,40,30,20,20,20)))
print(find_sequence_order((40,40,40,30,20,20,20,10)))
print(find_sequence_order((40,40,40,30,10,20,20)))
