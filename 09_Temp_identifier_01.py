temp = float(input("ENTER THE TEMPERATURE : "))

bool_flag = False;

if (temp < -273 or temp == -273 or (temp > -273 and temp < 0)):
    print("INVALID TEMPERATURE")