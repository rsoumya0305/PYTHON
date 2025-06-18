n=int(input())
list=[]
new_list=[]
for i in range(n):
    temp=int(input("enter numbers:")) 
    list.append(temp)
print(list)
for i in list:
        if(i%5==0 and i%3==0):
            new_list.append(i)
print(new_list)    