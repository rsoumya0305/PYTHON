'''add confirmed guets to list
   remove  a guest who cancels
   check if a friend is on list
   sort and print the final guest list
'''
guest=['soumya','hi','hlo','bye','ok']
while(True):
    print("***********menu**********")
    print("1.add confirmed guets")
    print("2.remove  a guest")
    print("3.check if a friend attending party or not")
    print("4.view the final guest list")
    print("5.exit")

    choice=int(input("enter your chioce:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            guestname=input("enter guest name:")
            guest.append(guestname)
            print(f'{guestname} is added to guest list')
        if(choice==2):
            cancelledguest=input("enter cancelled guest name:")
            if(cancelledguest in guest):
             guest.remove(cancelledguest)
             print(f'{cancelledguest} is removed from guest list')
            else:
               print(f'{cancelledguest} is not in  guest list')
        if(choice==3):
            checkguest=input("enter guest name:")   
            if(checkguest in guest):
              print(f'{checkguest} is attending')
            else:
               print(f'{checkguest} is not attending')
        if(choice==4):
            if(len(guest)==0):
              print("list is empty")
            else:
              guest.sort()
              print("final list")
              print(guest)
        else:
           print("enjoy party")
           break
    else:
       print("invalid input")
       
           
               

              
                   