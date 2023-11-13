WHITE = '\u001b[47m'
BLACK = '\u001b[48m'
END = '\u001b[0m'


def pattern():
    for i in range(10):
        if i < 5:
            print(f'{WHITE}{"  " * (10 - i * 2)}'
                  f'{BLACK}{"  " * (i * 4)}'
                  f'{WHITE}{"  " * (20 - i * 4)}'
                  f'{BLACK}{"  " * (i * 4)}'
                  f'{WHITE}{"  " * (10 - i * 2)}'
                  f'{END}')
        else:
            print(f'{WHITE}{"  " * (i * 2 - 10)}'
                  f'{BLACK}{"  " * (40 - i * 4)}'
                  f'{WHITE}{"  " * (i * 4 - 20)}'
                  f'{BLACK}{"  " * (40 - i * 4)}'
                  f'{WHITE}{"  " * (i * 2 - 10)}'
                  f'{END}')
    print(f'{WHITE}{"  " * 40}{END}\n')
    for i in range(11):
        if i < 5:
            print('*' * (5 - i) * 2,
                  ' ' * (2 * i) * 2,
                  '*' * (5 - i) * 4,
                  ' ' * (2 * i) * 2,
                  '*' * (5 - i) * 2)
        else:
            print('*' * (i - 5) * 2,
                  ' ' * (10 - i) * 4,
                  '*' * (i - 5) * 4,
                  ' ' * (10 - i) * 4,
                  '*' * (i - 5) * 2)
