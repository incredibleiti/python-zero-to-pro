num = 3
print(type(num)) #using inbuilt type to check type of the variable

fnum = 11.0
print(type(fnum))

print(3/2) #this is in Python 3, in python 2 we will drop the decimal
print(3//2) #this drops decimal and floors it
print(3**4) #this for power of 3
print(7%2)  #this is for knowing if number is odd or even

print(3*2+1)   #order is multiplication --> add
print(3*(2+1)) #order of preference is bracket --> add --> mul

bnum = 2
bnum+=10
print(bnum)

print(abs(-5)) #print the absolute value
print(round(3.756)) #rounds to nearest integer
print(round(3.756,1)) #rounds to the first digit after decimal
print(round(3.756,2)) #rounds to the first digit after decimal

print(2==2) #true
print(3>2) #true
print(3<2) #false
print(3!=2) #true

#Using the casting

num_1 = '100'
num_2 = '200'

print(num_1 + num_2)

num_1=int(num_1)
num_2=int(num_2)

print(num_1 + num_2)
