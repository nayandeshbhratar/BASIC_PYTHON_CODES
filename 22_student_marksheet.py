choice = 'Y'
grade = 0 #TAKING GRADE INITIALLY AS ZERO OR NULL
while choice == 'Y' :
    print("################# STUDENT SERVER ################")
    print("ENTER THE FOLLOWING DETAILS TO DISPLAY MARKSHEET")
    name      = input("ENTER THE STUDENT NAME : ")
    roll_no   = int(input("ENTER THE STUDENT ROLL NUMBER : "))
    year      = input("ENTER THE YEAR : ")
    depart    = input("ENTER THE DEPARTMENT : ")
    semester  = input("ENTER THE SEMESTER : ")
    #TAKING MARKS OF 5 SUBJECT AS INPUT FROM END USER
    sub1 = float(input("ENTER THE MARKS OF SUBJECT 1 : "))
    sub2 = float(input("ENTER THE MARKS OF SUBJECT 2 : "))
    sub3 = float(input("ENTER THE MARKS OF SUBJECT 3 : "))
    sub4 = float(input("ENTER THE MARKS OF SUBJECT 4 : "))
    sub5 = float(input("ENTER THE MARKS OF SUBJECT 5 : "))
    #CALCULATING TOTAL SUM OF 5 SUBJECT 
    total = float(sub1 + sub2 +sub3 +sub4 + sub5)
    #CALCULATING PERCENTAGE 
    percentage = float((total/500.0)*100)
    # MARKS WISE GRADE CONDITIONS :
    if percentage >= 85.0 and percentage <= 100.0 :
        grade = "A+"
    elif percentage < 85.0 and percentage >= 75.0 :
        grade = "A"
    elif percentage < 75.0 and percentage >= 60.0 :
        grade = "B"
    elif percentage <= 50.0 and percentage > 60.0 :
        grade = "C"
    elif percentage <= 40.0 and percentage < 50.0 :
        grade = "D"
    else :
        grade = "F"

    # PRINTING THE MARKSHEET OF THE STUDENT :

    print(f'''
    ############### STUDENT MARKS SERVER ###############
    ----------------------------------------------------
    [STUDENTS DETAILS]
    ----------------------------------------------------
    1. NAME                 :   {name}
    2. ROLL NUMBER          :   {roll_no}
    3. YEAR                 :   {year}
    4. DEPARTMENT           :   {depart}
    5. SEMESTER             :   {semester}
    ----------------------------------------------------
    [SUBJECT WISE MARKS]
    1. SIGNAL PROCESSING    :   {sub1}
    2. EMF                  :   {sub2}
    3. PYTHON PROG          :   {sub3}
    4. ENG. MATHEMATICS     :   {sub4}
    5. SOFT SKILLS          :   {sub5}
    ---------------------------------------------------
    [TOTAL]                 :   {total}
    [PERCENTAGE]            :   {percentage}
    [GRADE]                 :   {grade}
    ---------------------------------------------------
    ''')
    choice = input("Do you want to order anything else Y/N \n")
    if choice == 'Y':
        continue
    else:
        break