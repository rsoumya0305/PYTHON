n=input()
m=input()
list=[]
for i in range (len(n)):
    if(n[i]!=m[i]):
        list.append(i)
print(list)
