# anything which comes inside the inverted commas is called string 
# ctrl + s for save 
# ctrl + / for comments  
# numbers is know as integers in python and you dont use commas during print 
 

print("hello world") 
print(4)

# any you use to store data 

# declariation
name : str  
# initilization
name = "uzair"  

# dont start var name with number
# pre define name cant be use as a var
# you cant use space
# you cant use special character

# make clear var names
# if you define datatype of any var you have to store same type of data init

# f" uzair {var} "  syntax
message : str =  "    ahmed   "
print(message.strip())

url: str = input("Write your URL: ")

if url.startswith('http://'):
    print(url.removeprefix('http://'))
elif url.startswith('https://'):
    print(url.removeprefix('https://'))
else:
    print("Invalid URL")


# num : int; num1 :int; num2 : int  = 87,64,67
# print(num,num1,num2) 
# Using type hints for individual variables

num: int
num1: int
num2: int

# Assigning values to the variables
num, num1, num2 = 87, 64, 67

print(num, num1, num2)
