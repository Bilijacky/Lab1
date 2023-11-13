RED = '\u001b[41m'
GREEN = '\u001b[42m'
YELLOW = '\u001b[43m'
END = '\u001b[0m'


def flag():

    print("Флаг")
    for i in range(6):
        if i < 3:
            print(f'{GREEN}{"  " * 5}{YELLOW}{"  " * 9}{END}')
        else:
            print(f'{GREEN}{"  " * 5}{RED}{"  " * 9}{END}')
