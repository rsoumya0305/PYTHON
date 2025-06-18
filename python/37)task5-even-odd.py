n=int(input())
list=[]
new_list_even=[]
new_list_odd=[]
for i in range (n):
    temp=int(input("enter numbers:"))
    list.append(temp)
for i in list:
        if(i%2==0):
           new_list_even.append(i)
        else:
           new_list_odd.append(i)
print(new_list_even)
print(new_list_odd)