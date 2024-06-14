# Lets Understand the length operator and Input operator
# Calculate the length of your first name 
print('Please insert your name :')
name = input()
length_of_name = len(name)
print('Your name is of length:',length_of_name)
print( length_of_name//2,'===> This is the half length of your name calculated by using integer division ')

#input operator only takes string 
print("Plese insert a number")
number = input()
print(len(number))
#This statement will print the string length of the number that you have entered as it a string

# Now lets try the same thing although this time we will change input to integer 
number1 = int(42)
print('Please enter the number 42')
number2 = input()
print(number1==number2)
print("This will return False since the default datatype of the input function is always string ")
print("")
print(number1 == int(number2),"=============> Now after changing the datatype this shall be true")


