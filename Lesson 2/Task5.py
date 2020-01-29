n = input('Please enter your name: ')
    
while True:
    p = input('Please enter password: ')   
    if p == 'python':
        break
    else:
        print('Password for user ' + n + ' is incorrect')
        print('Please try again...')
        
print('Password for user ' + n + ' is correct!')