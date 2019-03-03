# # # ####

# import_os.path as os_path


from os import path, makedirs

# #########################
# 1) Python Absoulute path
# ########################
#
# current absolute path

# file_path = r"c:\repos\Library"
# current_file_path = path.abspath(__file__)
# print(current_file_path)
# print(path.dirname(current_file_path))
# print(path.basename(current_file_path))


# Get current directory
current_directory = path.dirname(path.abspath(__file__))
# print(current_directory)

# Concat file path

jason_file_path = path.join(
    current_directory, 'test_demo', 'jason_file', 'parse_jason_dat.jason'
)


# if path.exists(jason_file_path):
#       print("hello JSON")

#
xml_file_path = path.join(
    current_directory, 'test_demo', 'xml_file', 'parse_xml_data.xml'
)
#
# if path.exists(xml_file_path):
# print("hello XML")
#
text_file_path = path.join(
    current_directory, 'test_demo', 'xml_file', 'parse_xml_data.xml'
)
# print("hello text")

#

CSV_file_path = path.join(
    current_directory, 'test_demo', 'xml_file', 'parse_xml_data.xml'
)
# print("hello csv")

#
#
# class_09 = path.join(
#     current_directory, 'test_demo', 'class_09', 'test_dr', 'whynot dr'
# )
# print(class_09)
#
if not path.exists(path.dirname(text_file_path)):
    makedirs(path.dirname(text_file_path))

file_data = "This is my classo9 file, which is created for test purpose,"



with open(text_file_path, 'w+') as text_file:
     text_file.writelines(file_data)

from pprint import pprint

# with open(text_file_path, 'r+') as text_file_read:
# data = text_file_read.readlines()
# pprint(data, width=120/

# if path.exists(text_file_path):
#     print("exists")

# with open(text_file_path, 'r+') as text_file_read:
#     for line in text_file_read:
#          print(line.replace("\n", ''))

def generator_parse_file(file_path):
    with open(file_path, 'r+') as text_file:
        for line in text_file:
            yield line.replace("\n", '')

for i in generator_parse_file(text_file_path):
    print(i)

#

