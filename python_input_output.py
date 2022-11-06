# Hash is used to comment code in Python
# Declare and Assign variables in Python

int_var = 10
float_var = 18.25
string_var = 'This is String' # or another way is "This is string"
Bool_var = True # if we want to assign false it should be False

# Function in Python for Output
# Function may or may not accept some parameter
print('Hello World')

# Print variable values in Python


print("Print value of Int_var = ",int_var," - Result Done !!")
print("Print value of Float_var = ",float_var," - Result Done !!")
print("Print value of String_var = ",string_var," - Result Done !!")
print("Print value of Bool_var = ",Bool_var," - Result Done !!")

# How to check Datatype of any variable
# We can use type() function

print("Type of input variable = ?", type(int_var))
print("Type of input variable = ?", type(float_var))
print("Type of input variable = ?", type(string_var))
print("Type of input variable = ?", type(Bool_var))

# How to do type casting in Python 
# int(),float(), str() , bool()
int_var = int_var + 10 # int_var = 10 + 10 and in next step int_var will be 20
casted_int_var = float(int_var)
int_var = float(int_var)  # Same as above line
print("Int to float type casting for int var = ",casted_int_var)

casted_float_var  = int(float_var)
print("Float to Int type casting for int var = ",casted_float_var)

numeric_str = "123"
#numeric_str = numeric_str + 50 # is it valid - No. As it is string datatype.cannot do '123' + 
print("Value of numeric str = ",numeric_str)
numeric_str = int(numeric_str) + 50
print("Value of numeric str = ",numeric_str)

# How to take inputs on Python?
# we can use input function

#name  = input()
#age = input()
#print("User Name = ",name)
#print("User Age = ",age)

# another way to take user input with custom message
# convert type of data during input
name  = input("Enter the value for name  = ")
age = int(input("Enter the value for age  = ")) #Func within func
print("User Name = ",name)
print("User Age = ",age)

print("Type of name = ",type(name))
print("Type of age = ",type(age))




