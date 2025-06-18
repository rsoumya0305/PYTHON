'''declare a list of grocery items and read input from user 1 to 5 
1)to display the list of items in sorted way
1)kg
2)lit
3)dozen

2)take input from user and add item to cart
give the card items 
3)to update the quantity or item present in cart 
4)generate bill including item names item quantity and price and
    if final bill amount is greater then 1000 user gets 10% discount
    if user purchases any item more than 10kgs
    reduce then amount of 1kg from that particular item price 
    if user purchases any particular item add buy1 and get1 offer
5)add 25%gst to overall bill and print bill'''


list=['rice','oil','dal']
cart=[]
choice=int(input("choice:"))
if (choice>=1 and choice<=6):
    if(choice==1):
        list.sort()
        print(list)
    if(choice==2):
        temp=input("enter the item you need to enter in cart:")
        cart.append(temp)
    print(f"cart items are:{cart}")
    if(choice==3):
        update=("enter you want to update:")
        list.pop()
    print(list)
    if(choice==4):
      bill=int(input())
      if(bill>1000):
            discount=(bill*10/100)
            discount=bill-discount
      print(f"dicount={discount}")

        


