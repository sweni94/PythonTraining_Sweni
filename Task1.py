#1.Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.

a,b, c= "exel", 5.4, 4
print(a,b,c)
#2. Create a variable of type complex and swap it with another variable of type integer.

com = 3+2j
int1 = 100
com, int1 = int1, com
print ("num_1:",com,"num_2:",int1)

#3. Swap two numbers using a third variable and do the same task without using any third variable.


int1 = 123
int2 = 567
#swaping without using third variable
int1, int2 = int2, int1
print ("num_1:", int1, "num_2:", int2)
#swaping using third variable
a = 98
b = 78

c = a
a = b
b = c
print ("After swapping, the value of a is {} & the value of b is {}".format(a,b))

#4.Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.

f_name=input("Enter your first name:")
age = int(input("Enter your age:"))
print("my name is {} and I'm {}".format(f_name,age))

#5.Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
#another variable called z. Add 30 to z and store the output in variable result and print result as the
#final output.

print("enter 2 numbers between 1-10")

int1=int(input())
int2=int(input())
z= int1+int2
result= z+30
print(result)

#6.Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc

var = eval(input("Enter a value: "));
print("The data type of the variable is :", type(var))

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
#UPPERCASE.

#Upper Camelcase
FirstName = "Sweni"
#lower Camelcase
lastName = "Thakkar"
#Snakecase
email_address = "sweni.m.thakkar@gmail.com"
#Uppercase
MOBILENUMBER = 1234567890

#8.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
#again. Will it change the value? If Yes then Why?

a = 12
print(type(a))
a = 1.2
print(type(a))

#Yes,it will change the data type according to the value assigned. Because Python is an interpreted language, which runs line by line. So the latest value assigned to variable 'a' that data type will be retained.
