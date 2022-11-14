# Write a program to print a table of 9
num=9
i=1
while(i<=10):
    result=num * i
    print('Table of 9 is : ',result)
    i +=1

#Print the numbers from for loop and start them from value 10

for i in range(10,0,-1):
    print(i)

# Create empty list, check its length and add elements to it

l2 = []
print(type(l2))
print ('intial length of l2 is :',len(l2))

l2.append(1)
print("l2 is now : ",l2,'and length is : ',len(l2))
l2.append(2)
print("l2 is now : ",l2,'and length is : ',len(l2))
l2.append(3)
print("l2 is now : ",l2,'and length is : ',len(l2))

l1=[1,2,3,5]
# Compare 2 lists
if (l1 == l2):
    print("Lists are equal")
else:
    print("Lists are not equal")

# Concat 2 lists

l3 = l1 + l2
print("Values of l3 are :",l3)

# Access 4th element of  list
print("Fourth element is: ",l3[3])

#How to update value of list index item

l3[3] = 0
print(l3)

# how to print elements using length
for num in range(0,len(l3)):
    print(l3[num])

#How to print last value of list?
print('Last Value of list is:',l3[-1])

#How to print list in reverse
l9 = [26,10,1991,24,0,1945]
print(l9[-1::-1])
print(l9[:4])
print(l9[4:])

#Create empty Dict, check type and add elements
#How to insert values in Dictionary

d1 = {}
print(type(d1))
d1={'key1':'1','key2':'2','key3':'3'}
print(d1)

## Check the length of dictionary
print('Length of Dict is :',len(d1))
# how to access value of a particular key
print('Value of particular key is:',d1['key1'])
# how to update value on a particular key
d1['key2'] ='Updated'
print(d1)
# How to get the keys from a dictionary
print('keys from dict are:',d1.keys())
# How to get the values from a dictionary
print('values from dict are:',d1.values())
# How to iterate on dictionary?
for k,v in d1.items():
    print(k)
    print(v)
# Compare dictionary ??
d2 = {'key4':4,'key5':5,'key6':6}
if (d1 == d2):
    print('Dict are equal')
else:
    print('Dict are not equal')
# how to delete specific key value pair from dictionary
del d1['key2']
print(d1)

# how to check if key exists in dictionary or not??
if 'key9' in d2.keys():
    print('Key is there')
else:
    print('Key is not there')
