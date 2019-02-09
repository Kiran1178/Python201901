"""
if <Condition>:
    statement

"""
number_01 =1
number_02 =2
number_03 =4

# if number_01 < number_02:
#     print('Number 02 is greater than Number01.')
#
# #if else
#
# if number_01 > number_02:
#     print("Number 01 is greater than Number02.")
# else:
#     print('Number 02 is greater than Number01.')

#if elif else

# if number_01 > number_02:
#     print("Number 02 is greater than Number 01.")
#
# elif number_02 < number_03:
#     print('Number 03 is greater than Number02.')
#
# else:
#     print('Number 02 is greater than Number01.')

# ## if
"""
if <Condition>:
    statement
    """
number_01 =8
number_02 =5
number_03 =6


if number_01 > number_02:
    if number_01 > number_03:
        print("Number 01 is max")
    else:
        if number_02 > number_03:
            print("Number 02 is max")
        else:
            print("Number 03 is max")

if number_01 < number_02 < number_03:
        print("Number 03 is max")

elif number_01 < number_02 and number_02 > number_03:
        print("Number 02 is max")

elif number_01 > number_02 and number_01 > number_03:
        print("Number 01 is max")

# ####################################################################################################################
# 2) Break abd continue
# ####################################################################################################################


"""
for i in range():
    print(i)
"""

# for Loop
for i in range(0, 5):
    print(i)

# while loop
number = 0
while number < 5:
    print(number)
    number += 1

#Do while loop (by default enter in loop)
number = 0
while True:
    if number > 5:
        break
    print(number)
    number += 1

# ####################################################################################################################
# 4) Nested loop
# ####################################################################################################################

for i in range(0, 5):
    for j in range(0, i):
        print(j, end="")
        print('')

# ####################################################################################################################
# 5) Control Looping
# ####################################################################################################################
# Do while loop (by default enters in loop)
# number = 0
# while True:
#   if number >5:
        break
    print(number)
    number +=1

for i in range(0, 11, 2):
    if i % 2 == 0:
        print(i)

# ####################################################################################################################
# Create Assignment using for or while loop

for i in range(0, 5):

    for j in range(0, 5):
        print("1", end=" ")
    print('')

#

# number = 0
# while True:
#     if number > 5:
#         break
#     print(number)
#     number += 1

for i in range(0, 11, 2):
    if i % 2 == 0:
        print(i)
#



for i in range(0, 5):

    for j in range(0,5):
        print(i%2,end='')
    print('')


#
for i in range(0, 5):

    for j in range(0, 5):
        print("1", end=" ")
    print('')
#

for i in range(0, 5):

    for j in range(0, 5):
        print("*", end=" ")
    print('')

#
#
#
# num=int(input(5))
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         print("1", end="")
# print('')
#
# #
#
#
# for i in range(0, 5):
#
#     for j in range(0, 5):
#         print("*", end=" ")
#     print('')
#
# #
#
# #
# for i in range(0, 5):
#
#     for j in range(0, 5):
#         print("1", end=" ")
#     print('')
#
# print("###########")


for i in range(0,6):
    for j in range(0, i+1):
        print(2**(j+1), end=" ")
    print(" ")


#
for i in range(0,5):
    for j in range(0, j+1):
        print (i%2, end=" ")
    print(" ")

