set_1 = {1,7,9,3,10}
print(set_1) #sets can print in any order

print(7 in set_1) #sets can also find but are more efficient

set_2 = { 9,10,4,98}
print(set_2.intersection(set_1)) #this will give us common

print(set_2.difference(set_1))  #this will give us the diffrence

print(set_1.union(set_2)) #this will give us combination

#create empty
empty_set = set()
print(empty_set)
