while True:
    print('Username:')
    name = input()
    if name != 'xyz':
        print('Invalid Username ! Try Again')
        continue
    print('Password:')
    password = input()
    if password =='abc':
        print('Congrats the login is successful! Enjoy your day')
        break
    else: 
        print('Invalid login')
        continue



