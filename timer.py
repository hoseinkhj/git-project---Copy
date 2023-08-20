import time
import  os
while True:
    choice = input('Do you want to start? (y/n)  ')
    if 'y' in choice.lower():
        h = int(input('Enter hour: '))
        m = int(input('Enter min: '))
        s = int(input('Enter second: '))
        total = ( h * 3600 ) + ( m * 60 ) + s
        for i in range(total,-1,-1):
            print('Timer start now: ')
            print(i)
            time.sleep(.3)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        print('End')
    elif 'n' in choice.lower():
        print('End')
        break
    else:
        print('Invalid input!!!')