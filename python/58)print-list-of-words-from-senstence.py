s=(input())
max=0
m=s.split()
print(m)
longest=''
for i in m:
    if(max<len(i)):
        max=len(i)
        longest=i
print(longest)

