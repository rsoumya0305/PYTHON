count=0
n=input()
upper=0
lower=0
digit=0
spcl=0
for i in n:
    if i.isupper():
        upper=upper+1
    if i.islower():
        lower=lower+1
    if i.isdigit():
        digit=digit+1
    else:
        spcl=spcl+1
print(upper)
print(lower)
print(digit)
print(spcl)
    
    