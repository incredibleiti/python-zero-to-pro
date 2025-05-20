students = {'name': 'abc', "age": 12, "birthplace": "Netherlands"}
print(students) #basic printing the dictionary
print(students['name']) #using the key to find value
print(students['age']) #this will print age value, doesnt matter "age" or 'age'

#using different data type as key
teacher = {1: "John", "lastname": "Doe", "subjects": ["English", "Maths"]}
print(teacher)
print(teacher[1])
print(teacher["subjects"])
