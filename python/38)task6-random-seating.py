n=int(input())
list=[]
new_list=[]
for i in range (n):
    temp=input("enter names:")
    list.append(temp)
print(list)
temp=list[2]
list[2]=list[3]
list[3]=temp
print(list)
    