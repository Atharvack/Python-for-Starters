# This is an example of flow control statements 
#IF , ELIF and ELSE
print('Enter your name:')
name = input()
print('Enter your age:')
age = int(input())

if age<=0:
    print("Man what the hell are you doing , talking from heaven are ya?")
elif 0 < age <= 10:
    print("BRO Grow up first !")
elif 10 < age <= 20 :
    print(" Hows the Job struggle going so far. Please Type your answer below :")
    input()
    print("Everything works out eventually !")
elif 20 < age <= 50 :
    print("I wont bother. Its time to get serious")
else :
    print("Yo Bro  , what the heck  that age is not supposed to be here . Run the program again!")
    