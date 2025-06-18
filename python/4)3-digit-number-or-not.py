n=int(input())
Res="3-digit" if (n<=-100 and n>=(-999) or (n<=999 and n>=(100))) else "Not 3 digit"
print(f"{n} is {Res}")


if(n<=-100 and n>=(-999) or (n<=999 and n>=(100))):
    print(f"{n} is 3-digit")
else:
    print(f"{n} is not 3-digit number")