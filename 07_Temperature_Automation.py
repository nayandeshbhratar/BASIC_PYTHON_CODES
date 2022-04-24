#TAKING TEMPERATURE FROM END USER IN DEGREE CELCIUS :
celcius    = float(input("ENTER THE TEMPERATURE IN DEGREE CELCIUS : \n"))
fahrenheit = float(1.8 * celcius)+32

#THIS WILL PRINT THE CONVERSION OF TEMPERATURE
print("Temperature in fahrenheit :\n", fahrenheit)

if fahrenheit > 98 :
    print("TURN ON AC")
elif fahrenheit < 98 and fahrenheit > 68 :#Getting weight from the user in kg
    print("TURN ON FAN")
else :   
    print("TURN OFF FAN AND AC")