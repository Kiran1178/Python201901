print("Hello World")
# # This is my single line comment
# print("hello") # this is print statement
# ##
# # abcd
# # efgh
# ###
# """
# This is class 02 file
# 1) Variable
# 2) Data Type: Integer, string, Boolean, None3)
# 3) Data structure:
#
# # ############################################################################################################
# # 2) Data type
# # ###########################################################################################################
#
# ###
# """
# integer_variable = 3
# print(integer_variable), id(integer_variable)
#
# # ### Integer
# integer_variable = 3
#
# print('integer')
# print(integer_variable, id(integer_variable))
#
# # ### string
# string_variable  ="This is my single line string."
# string_variable_2="This is my " \
#     "multi line string 01."
#
# string_variable_3 ="""
# This is my multi line string 02.
# I can write anything in this block.
# No one have any problem with that, isn't it?
# """
#
# print('string')
# print(string_variable)
#
# print('string_2')
# print(string_variable_2, type(string_variable_2), id(string_variable_2))
#
# print('string_3')
# print(string_variable_3, type(string_variable_3), id(string_variable_3))
#
# # ### Boolean
# true_flag = True
# false_flag = False
#
# # ### None
#
# none_variable =None
#
# print(true_flag, type(true_flag), id(true_flag))
# print(false_flag, type(false_flag), id(false_flag))
#
#
# # ### None
# none_variable = None
# print(none_variable, type(none_variable), id(none_variable))
#  # ###################################################
# # ###################################################
#
# # 2) Data structure
# # ##################################################################################
#
# # # List
# List_variable = [
#     'Kiran', 'Home', 123456789, 111 ,222, False
# ]
#
# print(List_variable)
# print(
#     type(List_variable[0]), type(List_variable[1]), type(List_variable[2]), type(List_variable[3]),
#     type(List_variable[4])
# )
# print(List_variable.index('Kiran'))
#
#
# print(len(List_variable))
# print(List_variable.count('Kiran'))
#
# integer_list = [3, 2, 7, 6,99,10]
# print(sorted(integer_list))
# integer_list.sort(reverse=True)
# print(integer_list)
#
# list_nested = [ "Kiran",
#                 [
#                     "SamarthTech",
#                     "Certview",
#                     [
#                         203000, 1039200
#                     ]]
# ]
# print(list_nested[1][2][0])
list_nested_02 = [
    [
        'test_1',
        ['test_2', 'test_3', ['test4']],
        'test_5',
        ['test_6', 'test_7'],
        'test_8',
        ['test_9', ['test_10']]
    ]
]

print(list_nested_02[0][4])










