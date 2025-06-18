n=int(input())
list=[]
output=[]
for i in range(n):
    temp=input("enter:")
    list.append(temp)
print(list)


for i in range(len(list)):
    if(i>=5):
        output.append("underexpressed")
    if(i<=5 and i>=15):
        output.append("normal")
    else:
        output.append("overexpressed")    
print(output)
