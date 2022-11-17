# Q16. Write a code that gives following as an output.iNeuroniNeuroniNeuroniNeuron

full_str ="iNeuron"
final_str = full_str * 4
print(final_str)

# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

num1 = int(input("Enter a number : "))
if(num1%2 == 0):
    print(num1,"Number is even")
else:
    print(num1,"Number is odd")

# Q22. Write a code to take the age of person as an input
# and if age >= 18 display "c". If age is < 18 display "I can't vote".

age = int(input("Please enter age : "))
if(age>=18):
    print("I can vote")
else:
    print("I can't vote")

#Q23. Write a code that displays the sum of all the even numbers from the given list.
#numbers = [12, 75, 150, 180, 145, 525, 50]

sum=0
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in range(0,len(numbers),1):
    if (numbers[i]%2 == 0):
        sum=sum + numbers[i]
    else:
        continue
print('Sum is:',sum)

# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))
if(num1>num2 and num1>num3):
    print("Greatest Number is :",num1)
elif(num2>num1 and num2>num3):
    print("Greatest Number is :",num2)
else:
    print("Greatest Number is :",num3)


#Q23. Write a code that displays the sum of all the even numbers from the given list.
numbers = [12, 75, 150, 180, 145, 525, 50]
sum_result = 0
for num in numbers:
    if(num %2 == 0):
        sum_result = sum_result + num
print('Total Sum is :', sum_result)
 

#Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]  
for num in numbers:
    if (num%5 == 0):
        if(num > 150):
            continue
    elif(num > 500):
    break 
    
#Q28. Write a code to get the desired output of the following
string = "Big Data iNeuron"
print(string[9:])

#Q37. Write a code to access the word "iNeuron" from the given list.

lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])



#Q29. Write a code to get the desired output of the following
#string = "Big Data iNeuron"
#desired_output = "norueNi"
#k=-7
#print(string[::-1])

#Q33. How can you print the below string?
# 'iNeuron's Big Data Course'
str1 = "'ineuron's Big Data Course'"
print(str1)

#Q37. Write a code to access the word "iNeuron" from the given list.

lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
print(lst[4][2])

#Q76. Write a Python program to find the factorial of a given number.

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
f = factorial(5)
print(f)

#Q77. Write a Python program to calculate the simple interest. 
#Formula to calculate simple interest is SI = (PRT)/100
si=1
def interest(p,r,t):
    si= ((p*r*t) / 100)
    return si
si = interest(100,2,1)
print('Simple Interest is',si)

#Q78. Write a Python program to calculate the compound interest. 
# Formula of compound interest is A = P(1+ R/100)^t.
p= 1200  
t= 2     
r= 5.4    
a=p*(1+(r/100))**t  
ci=a-p  
print(ci)

#Q79. Write a Python program to check if a number is prime or not.

num=int(input("Enter a number:"))

if(num%2==0):
    print('Even number')
else:
    print('Odd Number')
    
# Q80.Python program to check if the number is an Armstrong number or not
# take input from the user
num = int(input("Enter a number: "))
# initialize sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


    
    
#Q82. Write a Python program to interchange the first and last element in a list.
l7 =[1,2,3,4,5]
temp=l7[0]
l7[0]=l7[-1]
l7[-1]=temp
print(l7)


#Q83. Write a Python program to swap two elements in a list.
l7 =[1,2,3,4,5]
temp=l7[1] 
l7[1]=l7[2] 
l7[2]=temp
print(l7)
    
#Q86. Write a Python program to check if a string is palindrome or not.
str1=str(input('Enter the string:'))
if (str1 == str1[::-1]):
    print('String is palindrome')
else:
    print('String is not palindrome') 
    
    
#Q87. Write a Python program to remove i'th element from a string.
## Taking string input from user
myStr =  input('Enter the string : ')
c = int(input('Enter the index of character to be removed : '))

# removing character at the specified index
resStr = myStr[:c] +  myStr[(c+1):]

# Printing all strings... 
print ("Entered string : " + myStr)
print ("String formed by removing c'th character : " + resStr)

#Q88. Write a Python program to check if a substring is present in a given string.
str1 = input('Enter the string : ')
str2 = input('Substring to be searched: ')

if str2 in str1:
        print('Given substring is present')
else:
        print('Given substring is not present')

#Q91. Write a Python program to merge two dictionary.
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
     # Run code
dict1 = {'a': 1, 'b': 8}
dict2 = {'d': 3, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

#Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
#Input: list = [9, 5, 6]
#Output: [(9, 729), (5, 125), (6, 216)]
num=0
result = 0
def cube_tuple(list1):
    for num in list1:
        result = (num * num * num)
        return (num,result)
cube_tuple([9, 5, 6])
print(cube_tuple)

#Question 96 pattern

n = int(input("Enter the number of rows"))  
for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  
        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
  
        # ending line after each row  
        print() 
