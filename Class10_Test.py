# # ###
# #
# letter = input ("Please enter a letter:\n")
# if (letter == 'i'):
#     print ("am lettera vowela")
# elif (letter== 'a'):
#     print("am lettera vowela")
# if (letter == 'u'):
#     print ("am lettera vowela")
# elif (letter== 'e'):
#     print("am lettera vowela")
# if (letter == 'o'):
#     print('am lettera vowela')
# else:
#     print("am lettera vowela nye")
#
# if (letter=='i') | (letter=='a')|(letter=='u')|(letter=='e'):
#     print('am lettera vowela')
# else:
#         print('am lettera vowela')
# txt="Hello i have a Aieroplane"
# x=txt.split("hello", "i have a Aieroplane")
# print(x)
# #
# for i in v:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#
#         print('i')
#         print('e')
#         print('a')
#
#
# n=int(input("enter the number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number is not a palindrome!")

#

# NUMBERS = ["zero", "one", "two","three","four","five","six","seven","eight","nine",
#                "ten"]
# TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
#             "ninety"]
# HUNNITS = ["","hundred","thousand","million","billion","trillion"]
#
# n = eval(input("What is the number the you want to convert? "))
# def convert():
#     if n >= 20:
#         tens = n // 10
#         units = n % 10
#
#         if units != 0:
#             result = TENS[tens] + "-" + NUMBERS[units]
#         else:
#             result = TENS[tens]
#     else:
#         result = NUMBERS[n]
#
#     print (result)
#
# def convert2():
#     if n >=100:
#         tens2 = n//100
#         units2 = n%100
#
#         if units2 != 0:
#             result2 = HUNNITS[tens2] + "-" + TENS[tens2] + "and" + NUMBERS[units2]
#         else:
#             result2 = HUNNITS[tens2]
#     else:
#         result2 = HUNNITS[n]
#
#     print(result2)
# def main():
#     if n >=20 and n< 100:
#         x = convert()
#     if n >=100:
#         y = convert2()
#
# main()


def check_vowels():
    input_str = input("Enter string: ")
    str_without_space = input_str.replace(' ', '')
    if len([char for char in str_without_space if char in ['a', 'e', 'i', 'o', 'u']]) == len(input_str):
        print("input contains all the vowels")
    else:
        print("string does not have all the vowels")
#
def check_palindrom():
    num = input("Enter number")
    if num == num[::-1]:
        print("input is palindrome")
    else:
        print("input is not a palindrome")
check_palindrom()
#

def convert_Number_to_words():
    dicto = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9':'nine'}
    num = input("Enter number: ")
    try:
        for item in list(str(num)):
            print(dicto[item], end=' ')
    except KeyError:
        raise ("Invalid input")

