
#Step 1: Add the Basic String function to print
message = "Hello World"
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

#Step 5: Sample on url value
url = "https://www.google.com"
print(url)
#print top level domain
print(url[-4:]) #prints .com
print(url[:5])  #prtints https
print(url[::-1]) #reverses the string
print(url[12:18]) #just print name 
