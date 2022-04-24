#TAKING TERMPERATURE AS INPUT FROM END USER

#float type var to store temperature

temp = float(input("ENTER THE TEMPERATURE : "))

# CONDITION

if temp < -273 :
    print("INVALID TEMPERATURE")
elif temp == -273 :
    print("ABSOLUTE ZERO TEMPERATURE")
elif (temp > -273 and temp < 0) :
    print("TEMPERATURE BELOW FREEZING POINT")
elif temp == 0 :
    print("TEMPERATURE IS AT FREEZING POINT")
elif (temp > 0 and temp < 100) :
    print("TEMPERATURE RANGE IS NORMAL")
elif temp == 100 :
    print("TEMPERATURE IS AT BOILING POINT")
else :
    print("TEMPERATURE IS ABOVE BOILING POINT")