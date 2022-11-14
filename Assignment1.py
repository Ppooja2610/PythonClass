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

#Q77. Write a Python program to calculate the simple interest. 
#Formula to calculate simple interest is SI = (PRT)/100
si=1
def interest(p,r,t):
    si= ((p*r*t) / 100)
    return si
si = interest(100,2,1)
print('Simple Interest is',si)

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
        
#Q76. Write a Python program to find the factorial of a given number.

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num
f = factorial(5)
print(f)
