Job_Roles=['Full Stack Developer','Data Engineer','Java Developer','Data Analyst','HR','Data Scientist','Team Lead']
Can_App=[
    #Name,Mailid,contactno,job applied for
    {'Name':'Jyothi','Mail ID':'jyothi@gmail.com','Contact No':9234567890,'Job applied for':'Data Analyst'},
    {'Name':'Niharika','Mail ID':'niharika@mail.com','Contact No':9567893421,'Job applied for':'Java Developer'},
    {'Name':'Nadeem','Mail ID':'nadeem@gmail.com','Contact No':8975643290,'Job applied for':'Data Engineer'},
    {'Name':'Sravya','Mail ID':'sravya@gmail.com','Contact No':8125698353,'Job applied for':'Full Stack Developer'},
    {'Name':'Harshith','Mail ID':'harshith@gmail.com','Contact No':7892345910,'Job applied for':'HR'}
]
Shortlisted_App=[
    {'Name':'Jagadeesh','Mail ID':'abc@gmail.com','Contact No':7124987307,'Job applied for':'Tech Support'},
    {'Name':'Shraddha','Mail ID':'xyz@gmail.com','Contact No':8192374650,'Job applied for':'SQL Admin'}
]
Completed=[
    {'Name':'Jyothi','Mail ID':'jyothi@gmail.com','Contact No':9234567890,'Job applied for':'Data Analyst'},
    {'Name':'Niharika','Mail ID':'niharika@mail.com','Contact No':9567893421,'Job applied for':'Java Developer'}
]
#-----------------------------------------------------------------
def View_Details():
    print(f"Applied Candidates :")
    for i in Can_App:
        print(i)
    print("-------------------------------------------------------------------------------")
    print(f"Shortlisted Candidates :")
    for i in Shortlisted_App:
        print(i)
    print("-------------------------------------------------------------------------------")
    print(f"Finalized Candidates :")
    for i in Completed:
        print(i)
    print("-------------------------------------------------------------------------------")
def Shortlisted_Profile():
    Name=input("Enter the Candidate Name :")
    for Candidate in Can_App:
        if Candidate['Name']==Name:
            Temp=input("Enter Yes If Candidate's profile meets the criteria & Job Requirement else enter No :")
            Can_App.index(Candidate)
            if Temp in "Yes yes":
                print(f"Congratulations {Name}...Your profile is shortlisted")
            else:
                print(f"Hello {Name}...we regret to inform you that your profile is not shortlisted")
def Schedule_Call():
    Name=input("Enter the candidate name to schedule for the interview :")
    for Candidate in Shortlisted_App:
        if Candidate['Name'] == Name:
            Shortlisted_App.append(Candidate)
            print(f"Congratulations {Name} your profile is shortlisted & we are proceeding level 1 interview with our ")
    else:
        print(f"{Name}'s profile is rejected at CV Evaluation")
def Update_Status():
    Name=input("Enter the Name of the candidate :")
    Status=input("Enter Yes if qualifies in level-1 interview else enter no")
    if Status in "Yes YES yes":
        print(f"Congratulations {Name} you have been qualified in level-1")
    else:
        print(f"Hello {Name}, unfortunately you did not clear the level-1")
def Send_Offer_Letter():
    Name=input("Enter the Name of the Candidate :")
    if Name in Completed:
        print(f"Congratulations...Offer Letter has been sent to {Name} at {Name['Mail ID']}")
    else:
        print(f"{Name} not found in Finalized List")
while(True):
    print("1. To View the candidates applications,shortlisted applications,job roles.")
    print("2. To shortlist the profiles")
    print("3. Schedule an interview for shortlisted candidates")
    print("4. To update the status of their profile")
    print("5. Send Offer letters to the particular candidates")
    print("6. Exit")
    print("-------------------------------------------------------------------------------")
    choice=int(input("Enter your choice:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            View_Details()
        elif(choice==2):
            Shortlisted_Profile()
        elif(choice==3):
            Schedule_Call()
        elif(choice==4):
            Update_Status()
        elif(choice==5):
            Send_Offer_Letter()
        else:
            print("Thank you.....!")
            break