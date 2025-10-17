# Working with variables
x = 1 
y = "HELLO"

# error as variable name should starts from _ or alphabets
# 1Name = "priya" 

# case sensitivity {Name != name}
Name  = "p"
name  = "r"

# variable reassignment
a = 10 
print(a) #10
a = 20
print(a) #20

# data types
age = 20
weight = 42.5
name = "priya"
is_stdent = True
print(type(weight)) #float
print(type(is_stdent)) #bool

#type conversion 
age = 20 #age is integer here
age_float = float(age)
print(type(age_float)) #float

#concatenation
s = "100"
a = 10
# print(s + a) # error cos s is string data type, concatenation happen only for same datatype

#arithmatic operations
a = 10
b = 3
print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a // b) #floor division
print(a % b) #remainder or modulus
print(a ** b) #expo


