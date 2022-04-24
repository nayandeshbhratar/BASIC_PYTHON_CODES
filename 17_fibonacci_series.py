#PRINTING FIBONACCI SERIES BY USING FOR LOOP

size  = int(input("Enter the numbers of terms : "))
num1 = 0
num2 = 1


for count in range(size):
	print(num1)
	next_num = num1 + num2
	num2 = num1
	num1 = next_num
