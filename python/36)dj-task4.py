n=int(input())
list=[]
new_list=["dj","folk","western"]
for i in range (n):
    temp=input("enter songs:")
    list.append(temp)
print(list)
list.extend(new_list)
print(list)
list.reverse()
print(list)
