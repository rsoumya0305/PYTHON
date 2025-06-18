a=[1,2,3,2,3,1,4,2,3,6,7,6,8,8,9]
new_list=[]
for i in a:
    if i not in new_list:
        new_list.append(i)
print(new_list)