import numpy as np
from numpy.linalg import det
while True:
    try:
        print(' ')
        print('A formula do produto misto é: ( v1 X v2 )⋅v3')
        print(' ')
        x, y, z = map(float, input('Digite o vetor 1 (formato x,y,z): ').split(','))
        x1, y1, z1 = map(float, input('Digite o vetor 2 (formato x,y,z): ').split(','))
        x2, y2, z2 = map(float, input('Digite o vetor 3 (formato x,y,z): ').split(','))
        print(' ')
        print(f'Seu vetor 1: ({x} , {y} , {z})')
        print(f'Seu vetor 2: ({x1} , {y1} , {z1})')
        print(f'Seu vetor 3: ({x2} , {y2} , {z2})')
        print(' ')
        prosseguir = input('deseja prosseguir? S ou N: ')
        if prosseguir=='N':
            continue
        else:
            matriz = np.array([[x, y, z], 
                               [x1,y1,z1], 
                               [x2,y2,z2]])
            print(' ')
            print('Matriz:')
            for row in matriz:
                print(" ".join(str(elem) for elem in row))
            print(' ')
            determinante = det(matriz)
            print('O resultado da determinate dessa matriz é o produto misto dos vetores')
            print(' ')
            print(f'resultado da determinante = {determinante}')
        print(' ')
        stop = input('Quer parar? S ou N: ').upper()
        if stop=='S':
            break 

    except ValueError:
        print("Erro: Você deve não digitou os vetores corretamente")