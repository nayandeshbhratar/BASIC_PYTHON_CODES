#DECLARING ALL VARIABLES AS GLOBAL VARIABLE 
# FIRST FUNCTION DECLARE 
def employee_detail() :
    print("############ ENTER THE EMPLOYEE DETAILS ###########")
    global name,employee_id,depart,desig
    name        = input("ENTER THE NAME OF THE EMPLOYEE : ")
    employee_id = input("ENTER THE EMPLOYEE ID NUMBER : ")
    depart      = input("ENTER THE DEPARTMENT : ")
    desig       = input("ENTER THE DESIGNATION : ")
    
#SECOND FUNCTION DECLARE    
def salary_details() :
    print("############ ENTER THE SALARY DETAILS #############")
    global basic_sal,gross_sal
    basic_sal     = int(input("ENTER THE BASIC SALARY : "))
    hra           = float(input("ENTER THE HRA IN PERCENTAGE (%): "))
    ta            = float(input("ENTER THE TA IN PERCENTAGE (%) : "))
    da            = float(input("ENTER THE DA IN PERCENTAGE (%) : "))
    incentive     = int(input("ENTER THE INCENTIVES : "))
    pf_deduction  = int(input("ENTER THE PF DEDUCTION AMOUNT : "))
    tds_deduction = int(input("ENTER THE TDS DEDUCTION AMOUNT : "))
    gross_sal = basic_sal + ((hra/100)*basic_sal) + ((ta/100)*basic_sal) + ((da/100)*basic_sal) + incentive - pf_deduction - tds_deduction
    print("TOTAL SALARY : ", gross_sal)
    
#THIRD FUNCTION DECLARE    
def salary_certf() :
    print(f'''
    ----------------------------------------------------
    ############### SALARY CERTIFICATE #################
    ----------------------------------------------------
    [EMPLOYEE DETAILS]   
    ----------------------------------------------------
    1. NAME              :     {name}
    2. EMPLOYEE ID       :     {employee_id}   
    3. DEPARTMENT        :     {depart}
    4. DESIGNATION       :     {desig}
    5. BASIC SALARY      :     {basic_sal}
    6. GROSS SALARY      :     {gross_sal}
    -----------------------------------------------------
    #####################################################
    -----------------------------------------------------
    ''')
    
employee_detail()
salary_details()
salary_certf()