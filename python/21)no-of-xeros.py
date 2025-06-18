n=int(input())
count=0
temp=n
while(n!=0):
    r=n%10
    if(r==0):
        count=count+1
    n=n//10
print(f"no.of 0s in {temp}={count}")
