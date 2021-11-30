# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]= 15
print(x)
students[0].update({'last_name' : 'Bryant'})
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0].update({'y' : 30})
print(z)

#iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def iterate_dictionary(list):
#     for i in range(0, len(list), 1):
#         for x, y in list[i].items():
#             print(f" {x} - {y} ,")
# def iterateDictionary(myList):
#     for i in myList:
#         my_str = ''
#         for key, val in i.items():
#             my_str += f"{key} - {val}"
#             if key != list(i)[-1]:
#                 my_str += ", "
#         print(my_str)

def iterateDictionary(someList):
    for dict in someList:
        text = ""
        for key in dict:
            text += f'{key} - {dict[key]}, '
        print(text[:-2])

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

def iterate_dictionary2(list, key_name):
    for i in range(0, len(list), 1):
        for x, y in list[i].items():
            if x == key_name:
                print(y)
            

iterate_dictionary2(students, 'first_name')
iterate_dictionary2(students, "last_name")

# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

def print_info(dictionary):
    for x , y in dictionary.items():
        print(x, len(y))
        for i in range(0,len(y),1):
            print(y[i])

print_info(dojo)
