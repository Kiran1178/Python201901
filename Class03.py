"""
1) Data structure: Dictionary, Tuple, Set
Assignment

1) create dictionary of user data
2) Create list of user data dictionary with minimum of 10 user data
3) create 5 dictionaries which have list values
"""

# [] = List
# {} = Dictionary
# () = Tuple

dictionary_variable = {
    'name': 'Kiran',
    'address': 'home',
    'mobile_number': 7760675005
}
print(dictionary_variable)
print(dictionary_variable['name'])
print(dictionary_variable.get('mobile_number', "Key does not found."))
print(dictionary_variable.get('contact_number', "Key does not found."))

print(dictionary_variable.keys())
print(dictionary_variable.values())
print(dictionary_variable.items())

contact_no = dictionary_variable['mobile_number']
dictionary_variable.pop('mobile_number')
print(dictionary_variable)

print(dictionary_variable)
dictionary_variable['contact_no'] = contact_no
print(dictionary_variable)

dict_01 = [
    {'test1': 'test2', 'test3': 'test4'},
    {'test5': [
        {'test6': 'test7', 'test8': 'test9'},
        {'test10': 'test11', 'test12': 'test13'}
    ]
    }
]

dict_02 = {
    'test1': 'test2',
    'test3': [
        {
            'test4': 'test5',
            'test6': ['test7',
                      'test8'
                      ]
        },

        [{'test9': 'test10'}, 'test11',
         {'test12': 'test13',
          'test14': 'print_me'}]
        ,
        {'test15': 'print_me_2'}
    ]
}
print(dict_02)
print(dict_02['test3'][1][2]['test14'])
print(dict_02['test3'][2]['test15'])


dictionary_variable = {
    'name': 'Samarthview',
    'address': 'Vishrantwadi',
    'mobile_number': 7760675005}
print(dictionary_variable['name'],['address'],['mobile_number'])

dictionary_variable = {
    'name': 'Kakde',
    'address': 'Pune',
    'mobile_number': 7760675005}
print(dictionary_variable)

dictionary_variable = {
    'name': 'Inorbitmall',
    'address': 'Wadi,Pune',
    'mobile_number': 7760675005}

dictionary_variable = {
    'name': 'Inorbitmall',
    'address': 'Wadi,Pune',
    'company': 'Samarthview',
    'Class': 'Phyton03',
    'Locality': 'Sathebiscut company',
    'mobile_number': 8087004247}
print(dictionary_variable['name'],['address'],['company'],['Class'],['Locality'],['mobile_number'])











