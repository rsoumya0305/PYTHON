'''python program
1)display menu food items
2)tuple of prices with respect of food 
3)read input from user for ordering the food including the quantity
 if exists in the menu---confrim order 
 if not print the message
4)while billing , read phone no,feedback,read tip amount 
5)add 10% gst to the bill&print the if bill>0'''

list=["idli","dosa","puri","pulka","chapati"]
tuple=(20,30,25,55,45)
choice=int(input("enter your choice:"))
if(choice>=1 and choice<=5):
    if(choice==1):
        print(list)
    if(choice==2):
        word=input("enter word:")
        index=list.index(word)
        print(f"the price of {word}:{tuple[index]}")
    if(choice==3):
        item=input("enter the item to order:")
        quantity=input("enter quantity:")
        if item in list:
            print("order confirmed")
        else:
            print("item is not present")
    if(choice==4):
        phno=int(input("please tell your phone number:"))
        feedback=input("enter your feedback:")
        tipamount=input("tip amount is:")
    if(choice==5):
        bill=int(input("bill is:"))
        if(bill>0):
           gst=bill*18/100
        print(f"gst is :{bill+gst}")
else:
    print("invalid input")

         






