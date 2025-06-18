n=input()
g=0
c=0
gc=0
for i in range(len(n)):
    if (n[i]=='g'):
        g=g+1
    if (n[i]=='c'):
        c=c+1
gc=(g+c)/len(n)*100
print(gc)
if(gc>60):
    print("High GC")
if (gc<=40):
    print("Low GC")
else:
    print("moderate")


    
        