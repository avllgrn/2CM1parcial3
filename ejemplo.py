from os import system

def muestraMatriz(X,m,n):
    for i in range(m):
        for j in range(n):
            print(X[i][j],end='\t')
        print()

def matrizIzqDerArrAba(m, n):
    X = [[0 for j in range(n)] for i in range(m)]
    cont = 1
    for i in range(m):
        for j in range(n-1, -1, -1):
            X[i][j] = cont
            cont += 1
    return X

if __name__ == '__main__':
    system('cls')

    print('Rellenar de Derecha a Izquierda, Arriba a Abajo\n')
    m = int(input('Dame m '))
    n = int(input('Dame n '))
    M4 = matrizIzqDerArrAba(m, n)
    print('M4')
    muestraMatriz(M4, m, n)
    print('\n\n')
    input()
    system('cls')
