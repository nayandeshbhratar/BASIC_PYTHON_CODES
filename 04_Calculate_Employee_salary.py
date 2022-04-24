# INPUT NAME BASIC_SALARY DA = 0.9 * BS   HRA = 0.4 * BS  TA = 0.3 * BS

print("****************EMPLOYEE SALARY DETAILS**************")
name = input("ENTER THE NAME OF EMPLOYEE  :\n")
salary =  int(input("ENTER THE BASIC SALARY :\n"))


string_DA   = str(0.9 * salary)
string_HRA  = str(0.4 * salary)
string_TA   = str(0.3 * salary)


#PRINTING OUTPUT
print("\n****************PRINTING SALARY DETAILS***************\n")
print(salary)
print(string_DA)
print(string_HRA)
print(string_TA)