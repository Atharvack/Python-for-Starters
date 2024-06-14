print("Lets check two numbers:")
# here since the input always takes string , the number entered will be strings so the magnitude of this numbers wont be same the strings will be same.
number1 = float(input())
number2 = float(input())
if number1!=number2:
    print("The number you have entered are not equal ")
    if number1>number2:
        print(number1,":Number 1 is greater than number 2:",number2)
    else:
        print(number2,":Number 2 is greater than number 1:",number1)
else:
    print("The number you have entered are equal")
