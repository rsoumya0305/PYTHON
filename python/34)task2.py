n=int(input())
list=[]
new_list=[]
for i in range(n):
    temp=(input("enter toy names : "))
    list.append(temp)
print(list)
for i in list:
  if i not in new_list:
     new_list.append(i)
print(new_list)
for i in new_list:
    new_list.sort()
print(new_list)

