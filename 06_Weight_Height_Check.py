#Getting weight from the user in kg
weight =  float(input("[+]Enter your weight in KG : "))
pounds =  float(weight * 2.2)

#Printing the weight in pounds
print("[+]Your Weight in Pounds : ", pounds)

# Condition to check wether the person has appropriate weight or not 
# if <condition> :
#        statement
# else :
#        statement

if pounds < 120 :
    print("[+]You are under weight")
else :
    print("[+]Your weight is approriate")