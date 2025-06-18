n=int(input())
list=[]
for i in range (n):
      temp=int(input(f"enter the {i} element :"))
      list.append(temp)
print(list)
print(len(list))
print(max(list))
print(min(list))
print(sum(list))
print(sorted(list))
print(any(list))
print(all(list))


