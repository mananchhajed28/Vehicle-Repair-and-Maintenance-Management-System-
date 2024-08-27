import ssd
import random
print()
print()
print("\t\t\t\t\t\t\t\t\t\t\tWelcome To Automobile Service Station")
r=True
print('\n')
while r:
    choice=0
    print('\n')
    print("1. Total records")
    print()
    print("2. Customer details")
    print()
    print("3. Vehicle repair")
    print()
    print("4. Vehicle return after repair")
    print()
    print("5. Vehicle history")
    print()
    print("6. Vehicles to be repaired in service station")
    print()
    print("7. Exit")
    print()
    print()
    choice=int(input("Enter the Choice - "))
    if choice==1:
        print()
        print("All the details :")
        print()
        ssd.all_details()
    elif choice==2:
        print()
        print('1. Add details ')
        print()
        print('2. Check details by Customer S.No')
        print()
        print('3. Check details by vehicle number')
        print()
        print("4. Retrieve SNO number")
        print()
        print("5. Exit")
        print()
        choice=int(input('Enter the Choice - '))
        print() 
        if choice==1:
            print()
            name=input("Enter the customer name: ")
            address=input("Enter the customer address: ")
            mobile=int(input("Enter the Mobile number: "))
            print()
            sno=""
            for i in range (12):
                sno=sno+str(random.randint(0,9))
            sno=str(sno) 
            ssd.add_customer(sno,name,address,mobile)
            print(name+" Added As CUSTOMER ")
            print('customer number is ', sno)
            continue
        elif choice==2:
            print()
            sno=int(input('Enter customer S.No.: '))
            print()
            print()
            if not ssd.check(sno,1):
                print('Customer is not registered yet \n Please register and try again')   
            else:
                ssd.show_details(sno)
            

        elif choice==3:
            print()
            vehicle=input('Enter vehicle number:')
            print('\n')
            if not ssd.check(vehicle,2):
                print('No vehicle with vehicle number= '+vehicle)    
                  
            else:
                ssd.search_vc(vehicle)
            

        elif choice==4:
            print()
            mobile=int(input('Enter mobile number of the customer: '))
            print("\n")
            if not ssd.check(mobile,3):
                print('No such mobile number exists in the\
                    database\n Please check and try again' )    
            
            else:
                ssd.mobretrieve(mobile)
        elif choice==5:
            break
    elif choice==3:
        print()
        print()
        sno=input("Enter the sno of customer: ")
        if not ssd.check(sno,1):
            print('Customer is not registered yet \n Please register and try again')    
                
        else:    
            model=input("Enter the model of vehicle: ")
            vehicle=input("Enter the Vehicle number: ")
            print()
            repcode=['cd','ws','eg','bat','he','br','cs']
            repair_cost={'1.Chassis Dents': 8000, '2.Windshield': 20000,\
                         '3.Engine': 30000, '4.Battery': 2500,\
                         '5.Headlights': 5000, '6.Brake': 4000,\
                         '7.Cooling System': 3000}
            repair=list(repair_cost.keys())
            cost=list(repair_cost.values())
            repcode=['1.','2.','3.','4.','5.','6.','7.']
            for i in repair:
                print(i)
            print("Enter all that applies\nLeave empty when done")
            e = True
            total=0
            defect=''
            print()
            print()
            while e:
                c=input("Enter your choices one by one & leave if done: ")
                print()
                if c.isnumeric() in range (1,8):
                    c=int(c)
                    c-=1
                    total+=cost[c]
                    defect+=repcode[c]
                elif c=="":
                    e=False
            print()
            print("Amount needs to be paid by customer",total)
                
            ssd.vehicle(sno,model,vehicle,defect,total)


    elif choice==4:
        print()
        print()
        vehicle=input('Enter vehicle number: ')
        print()
        ssd.update(vehicle)
        
          


    elif choice==5:
        print()
        print()
        vehicle = input("Enter Vehicle Number - ")
        if not ssd.check(vehicle,2):
            
            print('No vehicle with vehicle number = ' +vehicle)    
                      
        else:
            print()
            print("Problem Number: ")
            print()
            ssd.history(vehicle)
    elif choice==6:
        print()
        print()
        print("Details Of Vehicles yet to be repaired")
        ssd.nottaken()
    elif choice==7:
          break











