# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andrey'
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")

iterateDictionary(students)

# Get Values From a List of Dictionaries
def iterateDictionary2(key, value):
    for i in range(len(students)):
        print(students[i]['first_name'])

iterateDictionary2('first_name', students)

def iterateDictionary2(key, value):
    for i in range(len(students)):
        print(students[i]['last_name'])

iterateDictionary2('last_name', students)

# Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def prinInfo(some_dict):    
    for i in some_dict:
        if i == 'locations':
            print(f"{len(some_dict['locations'])} LOCATIONS")
            for j in some_dict['locations']:
                print(j)
        else:
            print(f"{len(some_dict['instructors'])} INSTRACTORS")
            for j in some_dict['instructors']:
                print(j)
prinInfo(dojo)