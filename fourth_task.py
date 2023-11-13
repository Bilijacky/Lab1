from matplotlib import pyplot as plt


def ratio():
    A1 = 0
    A2 = 0
    with open('sequence.txt') as numb:
        massiv = [float(i) for i in numb.read().split()]
    for i in range(len(massiv)):
        if (massiv[i] >= 0 and massiv[i] <= 5):
            A1 += 1
        elif (massiv[i] <= 0 and massiv[i] >= -5):
            A2 += 2
    print('Множество чисел от 0 до 5 = ', A1)
    print('Множество чисел от -5 до 0 = ', A2)
    if A1 <= A2:
        p = A1 / (A2 + A1) * 100
        print(p, '/', 100 - p)
    else:
        p = A2 / (A1 + A2) * 100
        print(p, '/', 100 - p)
    sets = ['Числа от 0 до 5', 'Числа от -5 до 0']

    data = [A1, A2]

    fig = plt.figure(figsize=(10, 7))
    plt.pie(data, labels=sets, autopct='%1.2f%%')

    plt.show()
