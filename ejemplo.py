from os import system

def muestraMatriz(X,m,n):
    for i in range(m):
        for j in range(n):
            print(X[i][j],end='\t')
        print()

def matrizArrAbaIzqDer(m, n):
    X = [[0 for j in range(n)] for i in range(m)]
    cont = 1
    for j in range(n):
        for i in range(m):
            X[i][j] = cont
            cont += 1
    return X

if __name__ == '__main__':
    system('cls')

    print('Rellenar de Arriba a Abajo, Izquierda a Derecha\n')
    m = int(input('Dame m '))
    n = int(input('Dame n '))
    M4 = matrizArrAbaIzqDer(m, n)
    print('M4')
    muestraMatriz(M4, m, n)
    print('\n\n')
    input()
    system('cls')
