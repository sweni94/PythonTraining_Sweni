#1.Write a program in Python to perform the following operation:
#If a number is divisible by 3 it should print “Consultadd” as a string.If a number is divisible by 5 it should print “Python Training” as a string
#If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
#string.

num = eval(input("num: "))
if num % 3 ==0:
    print("Consultadd")
elif num % 5 == 0:
    print("Python Training")
elif num % 3 == 0 and num % 5 == 0:
    print("Consultadd-python Training")
else:
    print("The number is neither divisible by 5 nor 3")

#2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.


operation = int(input("Enter 1 for addition ,2 for subtraction, 3 for Division, 4 for multiplication, and 5 for Average: "))
if operation == 1:
    add = num1 + num2
    print ("addition is", add)
    if add < 0:
        print ("Negative")
elif operation == 2:
    sub = num1 - num2
    print ("substraction is", sub)
    if sub < 0:
        print("Negative")
elif operation == 3:
    div = num1 / num2
    print("division is",div)
    if div < 0:
        print("Negative")
elif operation == 4:
    product = num1 * num2
    print("product is", product)
    if product<0:
        print("Negative")
elif operation == 5:
    first = eval(input("enter first number: "))
    second = eval(input("Enter second number: "))
    average = (num1+num2+first+second) / 4
    print ("Average is", average)
    if average < 0:
        print("Negative")

#3. Write a program in Python to implement the given flowchart:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
average = (a+b+c)/3
print ("Average =", average)

if average > a and average > b and average > c:
    print ("Average is higher than a, b, c")
elif average > a and average > b:
    print ("Average is higher than a, b")
elif average > a and average > c:
    print ("Average is higher than a, c")
elif average > b and average > c:
    print ("Average is higher than b, c")
elif average > a:
    print ("Average is just higher than a")
elif average > b:
    print ("Average is just higher than b")
elif average > c:
    print ("Average is just higher than c")
else:
    print ("Average is smaller than a, b, c")

#4.Write a program in Python to break and continue if the following cases occurs:If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”

while True:
    num1 = int(input("Enter a number: "))
    if num1 >= 0:
        print ("Good Going")
        continue
    else:
        print ("It's Over")
        break

#5.Write a program in Python which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200.

result = []
for num in range(2000,3201):
    if num % 7 == 0:
        if num % 10 == 0 or num % 10 == 5:
            continue
        else:
            result.append(num)
print (result)

#6.What is the output of the following code examples?

-> x=123

for i in x:
	print(i)

O/p:	TypeError: 'int' object is not iterable

-> i = 0
   while i < 5:
	print(i)
	i += 1
	if i == 3:
	  break
	else:
	  print(“error”)

o/p:  0
      error
       1
      error
       2
-> 	count = 0
	while True:
		print(count)
		count += 1
		if count >= 5:
			Break

o/p: 0
     1
     2
     3
     4
#7. Write a program that prints all the numbers from 0 to 6 except 3 and 6.
Expected output: 0 1 2 4 5
Note: Use ‘continue’ statement

for i in range(0,6):
    if i == 3:
        continue
    print(i)

#8. Write a program that accepts a string as an input from the user and calculate the number of digits
and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2


sample = input("Enter alphanumeric characters: ")

letters_count, digits_count = 0, 0 
for char in sample:
    if ord(char) in range(48,58):
        digits_count += 1
    else:
        letters_count += 1
print ("Letters {}  Digits {}".format(letters_count, digits_count))

#9..Read the two parts of the question below:

#Write a program such that it asks users to “guess the lucky number”. If the correct number is
#guessed the program stops, otherwise it continues forever.


luckyno = 7
while True:
    number = int(input("Guess the lucky number: "))
    if number == luckyno:
        print("congratulation")
        break


#Modify the program so that it asks users whether they want to guess again each time. Use two
#variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
#to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
#The program continues as long as a user has not answered “no” and has not guessed the correct
#number)


luckyno = 7
while True:
    number = int(input("Guess the lucky number: "))
    if number == luckyno:
        print("congratulation")
        break

    answer = input("Wanna continue guessing? y / n: ")
    if answer == 'n':
        break
#10..Write a program that asks five times to guess the lucky number. Use a while loop and a counter.

luckyno = 7
counter = 1
while counter <= 5:
    
    number = int(input("Guess the {} number: ".format(counter)))
    if counter == 5 and number != correctNumber:
        print("Game Over!")
        break
    if number == correctNumber:
        print("Good Guess!")
    else:
        print("Try again")
    
    counter += 1
#11.In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.

correctNumber = 7
counter = 1
while counter <= 5:
    
    number = int(input("Guess the {} number: ".format(counter)))
    if counter == 5 and number != correctNumber:
        print("Sorry but that was not very successful.")
        break
    if number == correctNumber:
        print("Good guess!")
        break
    else:
        print("Try again")
    
    counter += 1