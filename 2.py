from enum import Enum
while True:
    while True:
        try:
            class converter (Enum):
                USD = 1
                EUR = 2
                CZK = 3
                PLN = 4
            x = float (input ( 'amount of money:'))
            p = converter [input ( 'currency:')]
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    if p == converter.USD :
        x1=x/24.58
        print(f'{x} UAN = {x1} USD')
    elif p == converter.EUR :
        x1=x/26.91
        print(f'{x} UAN = {x1} EUR')
    elif p == converter.CZK :
        x1=x/1.08
        print(f'{x} UAN = {x1} CZK')
    elif p == converter.PLN :
        x1=x/6.31
        print(f'{x} UAN = {x1} PLN')
    else:
        print('Non actual currency ')
    print(f'Do you want to restart your program?\nIf YES - enter \'1\'\n   NO  - enter smth else')
    answer = input()
    if answer == '1':
        continue
    else:
        break