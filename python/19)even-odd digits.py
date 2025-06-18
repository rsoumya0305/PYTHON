n=int(input())
r=""
evencount=0
oddcount=0
temp=n
while(n!=0):
    r=n%10
    if(r%2==0):
        evencount=evencount+1
    else:
        oddcount=oddcount+1
    n=n//10
print(f"the even digits in the {temp} ={evencount}")
print(f"the even digits in the {temp} ={oddcount}")
