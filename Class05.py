"""
Topics for class05

1) Comprehension
2) User defined Function

"""
# ########################################
# Comprehension
# ########################################

# # ## List Comprehension
#
# _odd = list()
# for i in range(1,10, 2):
#     _odd.append(i)
# print(_odd)
# #
# # __odd = [ i for i in range(1, 10, 2)]
# # print(__odd)
# #
# # for i in range(1, 10):
# #     if i % 2 ==1:
# #      _odd.append(i)
# #
# # __odd = [i for i in range(1, 10) if i% 2 ==1]
# # print(__odd)
#
# # ## Directory Comprehension
# from lib2to3.fixer_util import Name
#
# # sq = {}
# # number = [2,4,6,7,8,9,11]
# #
# # for num in number:
# #     sq[num] = num*num
# # print(sq)
# #
# # _sq = {num: num*num for num in number}
# # print()
#
# lables = ['Name', 'Age', 'Contact No']
#
# user_1 = ['Parth', 10, 9876543221]
# user_2 = ['Srikant', 12, 9876352411]
# user_3 = ['Kiran', 14, 9876543021]
#
# # op = list()
# # ["Name": "Parth"
#
# op = list()
# for user in [user_1, user_2, user_3]:
#     _user = dict()
#     for index in range(0, 3):
#         _user[lables[index]] = user[index]
#
#     op.append(_user)
# print(op)

# ###############
# User Defined function
# # ####################
# #
# # def greeting():
# #     """This is greetings function
# #     """
# #     print("Hello World")
# #
#
#
# def wild_card_args_greetings(*args):
#     """
#
#     :param args: List wild card arguments
#     :return:
#     """
#     print(args[0], args[1])
#
# # wild_card_args_function(*['test', 'test1']}
# def wild_card_kwargs_function(**kwargs):
#     """
#
#     :param kwargs: Dictionary wild card argument
#     :return:
#     """
#
#     for key, values in kwargs.items():
#         print(key, ": ", values)
#
# user_1={"Name": "Parth", "Age":10, "Contact No": 9867542321}
# wild_card_kwargs_function(**user_1)
#
#
# #
# #
# squares[]
#
# for i in range(1, 101):
#     Squares.append(i**2)
#     Squares2 = [i**2 for i in range(1, 101)]
#
#


import random
print([random.randint(1,1000) for x in range(1,16)])
