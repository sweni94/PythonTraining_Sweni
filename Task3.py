#1. Create a list of 10 elements of four different data types like int, string, complex and float.
L = [1,2,5.3,"Sweni",1+2j]
print(L)

#2. Create a list of size 5 and execute the slicing structure
L= [1,6.5,"Sweni",90,45]
L[2:4]

#3. Write a program to get the sum and multiply of all the items in a given list.
List1 = [1,4,5,6,7,8]
sum,product = 0,1
for i in List1:
    sum = sum + i
    product = product * i
print("Sum of the list is: ",sum)
print("product of the list is",product)

#4.Find the largest and smallest number from a given list.
List1 = [1,9,6,78,65]
print(max(List1))
print(min(List1))

#5.Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list.
List1 = [1,8,0,4,6,9,5,7]
new = []
for i in List1:
    if i%2!=0:
        new.append(i)

print(new)

#6.Create a list of elements such that it contains the squares of the first and last 5 elements between
1 and30 (both included).
List=[]
for i in range(1,31):
    List.append(i**2)
print(List[:5])
print(List[-5:])

#7.Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]

L1 = [1,3,5,7,9,10]
L2 = [2,4,6,8]
L3 = L1 + L2
print(L3)

#8)8. Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}

 a={1:10,2:20}
 b={3:30,4:40}
 a.update(b)
 print(a)

#9)9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
#and n(both 1 and n included).
 
n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x] = x*x

print(d)

#10) Write a program which accepts a sequence of comma-separated numbers from console and
#generates a list and a tuple which contains every number in the form of string.

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)






