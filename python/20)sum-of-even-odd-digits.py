n=int(input())
sumodd=0
sumeven=0
temp=n
while(n!=0):
    r=n%10
    if(r%2==0):
        sumeven=sumeven+r      
    else:
         sumodd=sumodd+r   
    n=n//10
print(f"the sum of even digits in the {temp} ={sumeven}")
print(f"the sum of even digits in the {temp} ={sumodd}")