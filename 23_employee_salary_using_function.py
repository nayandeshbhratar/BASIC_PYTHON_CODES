# DEFINING FUNCTION BY USING def 
def basic_salary() :
    salary = int(input("ENTER THE BASIC SALARY : "))
    hra = 0.4 * salary
    ta  = 0.3 * salary
    da  = 0.9 * salary
    incentive = 5000
    gross_sal = salary + hra + ta + da + incentive
    print("TOTAL SALARY : ", gross_sal)
basic_salary()