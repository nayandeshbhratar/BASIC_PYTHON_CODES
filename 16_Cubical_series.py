# PRINTING THE SQUARE SERIES OF EVEN NUMBEER.

size = int(input("ENTER THE NUMBER OF TERMS : "))
if size >= 0 :
    print("GENERAL SERIES OF [(num ** 3)-1] is : ")
for series in range (1,size) :
    print(((series) ** 3)-1, end="\t")
    print("\n")
else :
    print("INVALID INPUT")