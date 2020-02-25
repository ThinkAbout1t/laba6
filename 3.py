from enum import Enum
while True:
    while True:
        try:
            class month (Enum):
                January = 1
                February = 2
                March = 3
                April = 4
                May = 5
                June = 6
                July = 7
                August = 8
                September = 9
                October = 10
                November = 11
                December = 12
            class season (Enum):
                Winter = 1
                Spring = 2
                Summer = 3
                Autumn = 4
            s = int(input ( 'month:'))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    if s==1 or s==2 or s==12:
        print(season.Winter.name)
    elif s==3 or s==4 or s==5:
        print(season.Spring.name)
    elif s==6 or s==7 or s==8:
        print(season.Summer.name)
    elif s==9 or s==10 or s==11:
        print(season.Autumn.name)
    else:
        print('Non actual season')
    print(f'Do you want to restart your program?\nIf YES - enter \'1\'\n   NO  - enter smth else')
    answer = input()
    if answer == '1':
        continue
    else:
        break
