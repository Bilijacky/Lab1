def function():
    for i in range(10):
        if i < 9:
            print(9 - i, '|', sep='', end='')
            for j in range(9):
                if j != 9 - i:
                    print('. ', end='')
                else:
                    print('/ ', end='')
            print('\n')
        else:
            for z in range(10):
                print(z, '', end='')
    print('\n')
