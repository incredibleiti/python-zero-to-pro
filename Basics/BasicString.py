
#Step 1: Add the Basic String function to print
message = "Hello World"
print(message)

#single quote vs double quote
message = 'Learner\'s World' #escape by backslash or write with double quotes
print(message)

#Step 2: Adding the basic sub string manipulations examples

message_2 = "Thisisalongstring"
print(message_2[0]) #shows only character at index '0' (0 is the starting index)

# Step 3: Perform Slicing
print(message_2[0:5]) #0 till index 4 (5th index is not included)
print(message_2[:5]) #this is same as above, no start index mentioned before index after :
print(message_2[5:]) #This is from certain index to the end

#Step 4: Perform reverse and learn steps

message_3 = "LETS_CHECK_MORE"
print(message_3[::2])  # start and end index default and we print every second char
print(message_3[::-1]) #leave the start and end empty and just add -1 in the step

#Step 5: Sample on url values
url = "https://www.google.com"
print(url)
#print top level domain
print(url[-4:]) #prints .com
print(url[:5])  #prtints https
print(url[::-1]) #reverses the string
print(url[12:18]) #just print name 

#Step 6: Change the case of the string

print(message_3.lower()) #prints all in lower case
print(url.upper()) #prints all in upper

#Step 7: Let us count characters and find

print(url.count('w'))  #counts the occurence of w in whole string
print(url.find('w'))   #finds the first occurence and returns the index (int)
print(url.find('goo')) #finds the index of the word
print(url.find('abc')) #returns -1 since cannot be found, so handy when we need to find the string
new_url = url.replace('w','c') #replace but since replace returns a string due to inplace replacement, we make a copy
print(new_url)

message = message.replace('e','i') #in place can also work like this
print(message) #now original Hello world becomes Hillo World

#Step 8: Concatenate strings
name = "Learner"
print(message+ " " + name)
new_string = "Hello World to the {}".format(name) #using the format we can avoid keeping track of + and concatenation
print(new_string)
new_string1 = f"Hello World to the {name}" #using python 3.6x this can be one of the ways to do it
print(new_string1)

new_string1 = f"Hello World to the {name.upper()}" #one can also use in place methods so we can make name upper case
print(new_string1) #Hello World to the LEARNER

#Step 9: Using all attributes which are applicable

print(dir(name))
print(help(str)) #shows more information but needs to be on string
print(help(str.lower)) #shows more information on string and how it works
