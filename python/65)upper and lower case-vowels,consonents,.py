s=input()
l_v,l_c,u_v,u_c=0,0,0,0
for i in s:
   if i.isalpha():
        if i.islower():
            if i in "aeiou":
                l_v += 1
            else:
                l_c += 1
        else:  # uppercase
            if i in "AEIOU":
                u_v += 1
            else:
                u_c += 1
    
print(l_v)
print(l_c)
print(u_v)
print(u_c)
    