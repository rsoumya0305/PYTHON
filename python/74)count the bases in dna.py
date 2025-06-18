n=input()
d={'a':0,'g':0,'c':0,'t': 0}
for i in range(len(n)):
    if(n[i]=='a'):
        d['a']=d['a']+1
    if(n[i]=='t'):
        d['t']=d['t']+1
    if(n[i]=='g'):
       d['g']=d['g']+1
    if(n[i]=='c'):
       d['c']=d['c']+1
print(d)
