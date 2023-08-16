# 5. Program to Remove the Duplicate Items from a List:
## assuming a list with duplicate members
dup_list = [50,20,30,50,20,50,10,20]
unique_list = []
dup_flag = False
i = 0
while i < len(dup_list) - 1:
    j = 0
    dup_flag = False
    while j < len(dup_list):
        if i != j:
            if dup_list[i] == dup_list[j] :
                dup_flag = True
                break
            else:
                dup_flag = False
        j += 1
        if dup_flag == False:
            unique_list.append(dup_list[i])
i += 1
print('Unique Items {}'.format(unique_list))
