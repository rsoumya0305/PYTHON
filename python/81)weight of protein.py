n=input()
a=20
b=30
c=40
d=50
asum=0
bsum=0
f=0
for i in range(len(n)):
    if('a'==n[i]):
        asum=a+asum
    if('b'==n[i]):
        bsum=b+bsum
print(asum+bsum)

    