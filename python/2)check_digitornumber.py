n=int(input())
Res="digit" if (n<=9 and n>=(-9)) else "Number"
print(f"{n} is {Res}")


if(n<=9 and n>=(-9)):
    print(f"{n} is digit")
else:
    print(f"{n} is number")