def prime(n):
    for i in range(2,n-1):
      if(n%i==0):
         return"not prime"   
    return"prime"
result=prime(3)
print(result)