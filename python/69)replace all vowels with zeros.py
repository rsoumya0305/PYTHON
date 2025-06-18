n=input()
new=''
for i in n:
    if (i in "aeiou"):
        new=new+"0"
    else:
        new=new+i
print(new)