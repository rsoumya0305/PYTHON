n=int(input())
if(n>0):
    print(f"{n} is +ve Number")
if(n<0):
    print(f"{n} is -ve Number")
#ternry operator
Res="+ve Number" if (n>0) else "-ve Number"
print(f"{n} is {Res}")