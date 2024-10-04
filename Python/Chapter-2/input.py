a=input("Enter number 1: ")
b=input("Enter number 2: ")
print("number 1 is: ",a)
print("number 2 is: ",b)
print("Sum is: ",a+b)
# if i enter 1 and 2, the output will be: 12
# because the input function takes the input as a string
# and the + operator concatenates the two strings thus the result becomes 1+2=12


# So what can we do now?
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
print("number 1 is: ",a)
print("number 2 is: ",b)
print("Sum is: ",a+b)

# what we did here is changed the type of the input  to integer using the int() function