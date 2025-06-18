s={'1','2','html','css'}
n={'4','soum','2'}
print(s)
print(type(s))

#operations=since sets are unoredered cant access elements by index
print('2' in s)    #membership

s.add('3')         #adding
print(s)

s.update(n)        #in list,tuple we use extend,in set we use set
print(s)
 
s.remove('4')     #returns error if not presnt
print(s)

s.pop()           #removes random eement
print(s)

s.discard('22')   #if element not there no error prints original
print(s)

#s.clear()
#print(s)
 
        #operations

print(s|n)        #union
print(s&n)        #intersection
p={1,2,3}
q={2,3}
print(p-q)        #difference
print(p^q)        #symmetric difference
print(q.issubset(p))
print(p.issuperset(q))

