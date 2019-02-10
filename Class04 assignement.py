#
for i in range(0, 5):

    for j in range(0, 5):
        print("*", end=" ")
    print('')#

#
for row in range(6):
    for coloumn in range(5):
        if ((coloumn==0 or coloumn==4) and row!=0) or ((row==0 or row==3) and (coloumn>0 and coloumn<5)):
print("")

######################

for i in range(0,6):
    for j in range(0, i+1):
        print(2**(j+1), end=" ")
print(" ")





