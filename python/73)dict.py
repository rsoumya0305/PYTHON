d={101:'py',102:'hi',103:'bye'}
f={'rahul':2000,'raj':4000}
print(d)
print(type(d))
print(d[101])
print(d[102])


d[102]='nice'#updating value
print(d)

d[105]='okk'
print(d)
d[106]='aww'
d[107]='yes'
d[108]='no'
print(d)

d.pop(102)
print(d)
del d [101]
print(d)

print(len(d))
print(d.keys())        #1 method
print(d.values())      #2 method
print(d.items())       #3 return keys and values as tuple
b=d.copy()             #4 
print(b)
d.update(f)            #5
print(d)


