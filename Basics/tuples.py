tuple_1 = (1,2,3,4,5)
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

#tuples are immutable, means you cannot change them
#tuple_1[0] = 10 #this will give error
print(tuple_1)
print(tuple_2)

tuple_1.__add__(tuple_2)
print(tuple_1)

#create empty tuples

empty_tuple= tuple()
print(empty_tuple)