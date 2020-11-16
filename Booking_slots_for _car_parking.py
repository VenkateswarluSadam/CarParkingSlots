
A=["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"]
B=["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"]
C=["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"]
D=["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"]
lanes=[A,B,C,D]
l=["A","B","C","D"]
cars=[]
lanslot=[]
def Display_Lanes():    
    print("A:",*A)
    print("B:",*B)
    print("C:",*C)
    print("D:",*D)

def Book(lane,slot,car_no):
    lanes[lane][slot]="BOOKED"
    cars.append(car_no)
    lanslot.append((lane+1,slot+1))
    print("\nYOUR SLOT IS BOOKED NOW YOU CAN PARK YOUR CAR")
    return

def Vacancy(lane):
    freeslots=[i+1 for i in range(10)if lanes[lane][i]=="FREE" ]
    if len(freeslots):
        return freeslots
    else:
        return False

def Receipt(lane,slot,car_no):
    print('\n')
    print("LANE","SLOT_NO","STATUS","CAR_NO",sep='\t')
    print(l[lane],slot+1,lanes[lane][slot],car_no,sep='\t')
    print('\n')
    print("\nNOTE:please note  the LANE_NO&SLOT_NO to free the slot.")
    print("THANK YOU VISIT AGAIN\n")
    return

def Verify_Slot_Status():
    lane=int(input("\nChoose[1,2,3,4] the lanes[A,B,C,D]:"))
    slot=int(input("\nEnte slot-no[1-10] you want to verify:"))
    if lanes[lane-1][slot-1]=="FREE":
        print("\nFREE")
    else:
        print("\nBOOKED")
    return

def Verify_Car_Status():
    car_no=input("\nEnter the car-no:")
    for i in range(len(cars)):
        if car_no == cars[i]:
            print("\nTHIS VEHICLE IS PARKED..AT(lane,slot)-->",lanslot[i])
            break
    else:
        print("\nTHIS VEHICLE IS NOT PARKED YET...")
        
def Check_Allvacancies():
    print("\nVacancies are-->")
    print("\nLANE    SLOTS")
    for i in range(4):
        v=Vacancy(i)
        if v:
            print(l[i],":",*v)
        else:
            print(l[i],":",v)

def Free():
    lane=int(input("\nEnter the lane[1,2,3,4,5] :"))
    slot=int(input("\nEnter slot-no[1-10]:"))
    lanes[lane-1][slot-1]="FREE"
    print("THANK YOU VISIT AGAIN...\n")
    return

def Display_Cars():
    print("\nCars:")
    print(*cars,sep='\n')

    

def Customer_Request():
    Display_Lanes()
    lane=int(input("\nChoose[1,2,3,4] the lane[A,B,C,D] you want to park :"))
    vacant=Vacancy(lane-1)
    if vacant:
        slot=int(input(f"\nEnter the slot_no{vacant} you like to park:"))
        car_no=input("\nEnter the car_number:")
        Book(lane-1,slot-1,car_no)
        r=input("\nDo you want to print the receipt(y/n):")
        if r=='y':
            Receipt(lane-1,slot-1,car_no)
            return
        else:
            print("\nTHANK YOU VISIT AGAIN")
            return 
    else:
        print("\nSORRY THERE IS NO VACANCY ....")
    return

def User_Options():
    __doc__='''
               1.display_lanes
               2.Book A Slot
               3.Free A Slot
               4.Check Slot Status
               5.Check Car Status
               6.Check All Vacancies
               7.Display All Cars
               8. exit
               '''
    print(__doc__)
    userchoice=int(input("Choose an option:"))
    if userchoice==1:
        Display_Lanes()
    elif userchoice==2:
        Customer_Request()
    elif userchoice==3:
        Free()
    elif userchoice==4:
        Verify_Slot_Status()
    elif userchoice==5:
        Verify_Car_Status()
    elif userchoice==6:
        Check_Allvacancies()
    elif userchoice==7:
        Display_Cars()
    else:
        return True

if __name__=="__main__":
    while True:
        stop=User_Options()
        if stop:
            break
           
            
            
            
    
    
    
