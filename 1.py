Flag1,Flag2,Flag3=False,False,False
while True:
    while True:
        try:
            days = range (1, 32)
            mounths = range (1, 13)
            years = range (1901, 2020)
            d, m, y = int (input ( 'day:')), \
            int (input ( 'mounth:')), \
            int (input ( 'year:'))
            if y%4 == 0:
                if y in range(1901, 2021):
                    Flag3 = True
                if m in range(1, 13):
                    Flag1 = True
                if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d in range(1, 32):
                    Flag2 = True
                    break
                if (m == 2) and d in range(1, 30):
                    Flag2 = True
                    break
                if (m == 4 or m == 6 or m == 9 or m == 11) and d in range(1, 31):
                    Flag2 = True
                    break
                if Flag1 and Flag2 and Flag3:
                    break
            else:
                if y in range(1901, 2021):
                    Flag3 = True
                if m in range(1, 13):
                    Flag1 = True
                if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d in range(1, 32):
                    Flag2 = True
                    break
                if (m == 2) and d in range(1, 29):
                    Flag2 = True
                    break
                if (m == 4 or m == 6 or m == 9 or m == 11) and d in range(1, 31):
                    Flag2 = True
                    break
                if Flag1 and Flag2 and Flag3:
                    break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    if y%4 == 0:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
            if d == 31:
                print(f'Data: {1}.{m + 1}.{y}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d == 30:
                print(f'Data: {1}.{m + 1}.{y}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m == 2:
            if d == 29:
                print(f'Data: {1}.{m + 1}.{y}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m == 12:
            if d == 31:
                print(f'Data: {1}.{1}.{y+1}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m==12 or m == 5 or m == 7 or m == 8 or m == 10 or m==2:
            if d==1:
                print(f'P Data:{30}.{m-1}.{y}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d==1:
                print(f'P Data:{31}.{m-1}.{y}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
        if m==1:
            if d==1:
                print(f'P Data:{31}.{12}.{y-1}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
        if m==3:
            if d==1:
                print(f'P Data:{29}.{m-1}.{y}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
    else:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
            if d == 31:
                print(f'Data: {1}.{m + 1}.{y}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d == 30:
                print(f'Data: {1}.{m + 1}.{y}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m == 2:
            if d == 28:
                print(f'Data: {1}.{m + 1}.{y}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m == 12:
            if d == 31:
                print(f'Data: {1}.{1}.{y+1}')
            else:
                print(f'Data: {d + 1}.{m}.{y}')
        if m==12 or m == 5 or m == 7 or m == 8 or m == 10 or m==2:
            if d==1:
                print(f'P Data:{30}.{m-1}.{y}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d==1:
                print(f'P Data:{31}.{m-1}.{y}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
        if m==1:
            if d==1:
                print(f'P Data:{31}.{12}.{y-1}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
        if m==3:
            if d==1:
                print(f'P Data:{28}.{m-1}.{y}')
            else:
                print(f'P Data:{d-1}.{m}.{y}')
    print(f'Do you want to restart your program?\nIf YES - enter \'1\'\n   NO  - enter smth else')
    answer = input()
    if answer == '1':
        continue
    else:
        break