#Section 1 comment out below part first run it and understand the things going on
# spam = 0 
# while spam < 6:
#     print('Hello world times ,Counter:', spam)
#     spam = spam +1 

# # lets see if the code terminates or skips the while clause and moves ahead

# print("DID it terminate Y/N")
# input()

# #It does now lets make additional annoying loop

# #Section 2
# name = ''
# counter = 1 

# while name != 'your name':
    
#     print('Type your name:'*counter)
#     # input() #FOR ANNOYING LOOP
    
#     counter = counter + 1
#     name = input() # This will terminate when you enter 'your name' 
# print('Thank you')

#Section 3 same thing using break statement

while True:
    print('Type your name :')
    name = input()
    if name =='your name':
        break

print('Thank you')