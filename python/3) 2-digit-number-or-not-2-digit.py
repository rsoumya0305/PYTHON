n=int(input())
Res="2-digit" if (n<=-10 and n>=(-99) or (n<=99 and n>=(10))) else "Not 2 digit"
print(f"{n} is {Res}")


if(n<=-10 and n>=(-99) or (n<=99 and n>=(10))):
    print(f"{n} is 2-digit")
else:
    print(f"{n} is not 2-digit number")