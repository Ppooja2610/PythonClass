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

