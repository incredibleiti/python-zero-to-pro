#List majorly used in a lot of Leetcode questions
courses = ['python', 'math', 'physics']
print(courses) #prints the lists content 
print(len(courses)) #prints the length of the list
print(courses[0]) #to access the value at indx '0'
print(courses[2]) #if we know the length of list we can find last element
print(courses[-1]) #this is when you dont know the length of the list

#we covered some slicing in strings but here it is again

print(courses[0:2]) #start to end (not including that indx)
print(courses[:2]) #same as above
print(courses[1:]) #start and till the end

#Method to play with lists
courses.append('art') #this will append the item
print(courses) #inserts at the end

courses.insert(0,'english') #ths will insert english at index 0
print(courses)

courses_2 = ['music', 'politics'] #this is another list
# courses.insert(0,courses_2)

print(courses)
print(courses[0]) #now index 0 has a list itself
courses.extend(courses_2)
print(courses)

#using remove
courses.remove('music')
print(courses)
popped = courses.pop() #helps when we want list as stack
print(popped)

#reverse the list
courses.reverse()
print(courses)

#sort the list
courses.sort()

#Now let us try on int values
nums = [1,2,5,9,3,6]
nums.sort()
print(nums)
#reverse the sort
nums.sort(reverse=True)
print(nums)

#get back the sorted list in new list without modifying it
numslst = sorted(nums)
print(numslst)

#finding the min, max and sum
print(min(numslst))
print(max(numslst))
print(sum(nums)) #nums and numlst are same in this context but we get that idea

#finding the index of the num in the list

print(nums.index(9)) #index can only be used if we know the item exists else we get an error
print(10 in nums) #in this way we get true or false

for value in nums: #this prints all values in the list
    print(value)

for index,value in enumerate(nums): #this is printing like with index
    print(index, value)
print("=======================================")
for index, value in enumerate(nums, start = 3):
    print(index,value)

#convert the list to string (lets take courses back)
courses_string = '-'.join(courses_2)
print(courses_string)

#we can now split it as well
new_list = courses_string.split('-')
print(new_list)

#create an empty list
empty_list = list()
print(empty_list) 