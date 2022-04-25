# PRINTING STOCKS OF THE INVENTORY ITEMS 
choice = "Y"
bill = int(0)
# DECRALING VRIABLES FOR STOCKS OF SPARE PARTS WITHOUT USING ARRAY FUNCTION
item1_qty = 100
item2_qty = 200
item3_qty = 300
item4_qty = 250
item5_qty = 400
print("############### WELCOME THE MAHINDRA MOTOR'S ##################")
while (choice == "Y") :
	print('''
		ITEM NAME           PRICE       QUANTITY
	[1]  ENGINE 		200000		item1_qty
	[2]  SPARK PLUG 	500		    item2_qty
	[3]  DISK BREAK		10000		item3_qty
	[4]  BREAK			7000		item4_qty
	[5]  SHOCK UP'S 	5000		item5_qty

	''')
	order = int(input("ENTER YOUR ORDER NUMBER : \n"))
	quantity = int(input("ENTER THE NUMBER OF QUANTITY :\n"))
	if order == 1 :
		if quantity < item1_qty :
			bill = bill + (200000 * quantity)
			item1_qty = item1_qty - quantity
	elif order == 2 :
		if quantity < item2_qty :
			bill = bill + (500 * quantity)
			item2_qty = item2_qty - quantity
	elif order == 3 :
		if quantity < item3_qty :
			bill = bill + (10000 * quantity)
			item3_qty = item3_qty - quantity
	elif order == 4 :
		if quantity < item4_qty :
			bill = bill + (7000 * quantity)
			item4_qty = item4_qty - quantity
	elif order == 5 :
		if quantity < item5_qty :
			bill = bill + (5000 * quantity)
			item5_qty = item5_qty - quantity
	else :
		print("ENTER THE VALID ITEM NUMBER :\n")
	choice = input("DO YOU WANT TO ANYTHING ELSE Y/N : ")
	if choice == "Y" :
		continue
	else :
		break
print("THE BILL IS WITHOUT ANY TAXES : ", +bill)

if bill < 50000 :
    gst = (bill * 15 / 100)
    delTax = 200
    SBA = 10
    GETAX = 10
    print('''
    ######## BILL RECIPT #########
    COST         :  {BILL}
    GST OF 15%   :  {GST}
    DELIVERY TAX : {delTax}
    GIRL EDU TAX : {GETAX}
    SBA          : {SBA}
	-------------------------------
	TOTAL        : {bill + gst + delTax +GETAX + SBA}
	''')
else :
    gst      = (bill * 22.22 / 100)
    delTax   = 200
    SBA      = 10
    GETAX    = 10
    print('''
	######### BILL RECIPT ##########
	Cost             :   {bill}
    GST of 22.22     :   {gst}
    Delivery Tax     :   {delTax}
    Girl Edu Tax     :   {GETAX}
    SBA TAX          :   {SBA}
    ------------------------------
    TOTAL            :   {bill + gst + delTax + GETAX + SBA}
    ''')
print("TOTAL BILL IS : ", bill + gst + delTax + GETAX + SBA)