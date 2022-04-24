choice = 'Y'
bill = 0
while choice == 'Y':
    print(" \n############ WELCOME TO HOTEL TULI ############\n ")
    print(" \n############ Menu Card OF TULI   ##############\n ")
    print(" Item number \t| Item name \t\t\t\t | Price\t\t")
    print(" 1. \t\t| CHICKEN TANDOORI  \t\t | 200 /-  ")
    print(" 2. \t\t| SHAHI PANEER      \t\t | 120 /-  ")
    print(" 3. \t\t| CHICKEN BIRYANI   \t\t | 70 /-  ")
    print(" 4. \t\t| LASSI             \t\t | 70 /-  ")
    print(" 5. \t\t| MUTTTON BIRYANI   \t\t | 250 /-  ")
    print(" 6. \t\t| SHAHI CHICKEN     \t\t | 200 /-  ")

    order = int(input("\n Enter the number of order : "))
    if order==1:
        bill = bill + 200
        print("You ordered CHICKEN TANDOORI worth 200/-")
    elif order==2:
        bill = bill + 120
        print("You ordered SHAHI PANEER worth 120/-")
    elif order==3:
        bill = bill + 70
        print("You ordered CHICKEN BIRYANI worth 70/-")
    elif order==4:
        bill = bill + 70
        print("You ordered LASSI worth 70/-")
    elif order==5:            
        bill = bill + 250
        print("You ordered MUTTON BIRYANI worth 250/-")
    elif order==6:
        bill = bill + 200
        print("You ordered SHAHI CHICKEN worth 200/-")
    else:
        print("Enter valid item number\n")
    choice = input("Do you want to order anything else Y/N \n")
    if choice == 'Y':
        continue
    else:
        break
if bill> 100 and bill<500 :
    discount = 0.1 * bill
elif bill>500 and bill <1000 :
    discount = 0.15 * bill
elif bill>1000:
    discount=0.20 * bill
else:
    discount=0
# print("YOUR BILL IS", bill)
print("your bill is (including gst and discount):", (bill-discount)+0.18*(bill))  # gst is 18%
print("Thank You ;), Visit again")