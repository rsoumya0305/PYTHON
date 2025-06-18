'''read the list of inoput from users convert into word and print it'''
s=int(input())
list=[]
for i in range(s):
    c=input("enter charcters:")
    list.append(c)
print(c)
str="".join(list)
print(str)

