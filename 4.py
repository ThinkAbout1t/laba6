while True:
    while True:
        try:
            x = int(input('Enter your time: '))
            break
        except ValueError:
            print('Oops!  That was no valid number.  Try again...')
    x1 = x % 6
    if 0 <= x1 < 3:
        print('Green')
    elif 3 <= x1 < 4:
        print('Yellow')
    else:
        print('Red')
    print(f'Do you want to restart your program?\nIf YES - enter \'1\'\n   NO  - enter smth else')
    answer = input()
    if answer == '1':
        continue
    else:
        break