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


