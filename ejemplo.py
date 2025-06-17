from os import system

def generaLetras(nodos, letra):
    inicial = ord(letra.upper())    
    G = {}
    for i in range(nodos):
        G.update({i:chr(inicial)})
        inicial+=1
    return G

def ingresaPesos(W):
    nodos = len(W)
    print('Ingresa pesos de aristas')
    for i in range(nodos):
        for j in range(nodos):
            x = input(f'Ingresa peso entre {G.get(i)} y {G.get(j)} (Enter, si no hay) ')
            try:
                W[i][j] = int(x)
            except:
                pass

def inicializaQ(W, Q):
    nodos = len(W)
    for i in range(nodos):
        for j in range(nodos):
            if W[i][j]!=0:
                Q[i][j]=W[i][j]

def caminoMinimo(Q):
    nodos = len(Q)
    for k in range(nodos):
        for i in range(nodos):
            for j in range(nodos):
                Q[i][j] = min(Q[i][j], Q[i][k]+Q[k][j])

def muestraMatriz(X):
    nodos = len(X)

    print('\t', end='')
    for j in range(nodos):
        print(f'{G.get(j)}', end='\t')
    print()
    for i in range(nodos):
        print(f'{G.get(i)}', end='\t')
        for j in range(nodos):
            print(f'{X[i][j]}', end='\t')
        print()

if __name__ == '__main__':
    system('cls')
    
    nodos = int(input('Cuántos nodos tiene el grafo? '))
    letra = input('En qué letra comienza? ')
    system('cls')
    
    G = generaLetras(nodos, letra)
    W = [[0 for j in range(nodos)] for i in range(nodos)]
    Q = [[float('inf') for j in range(nodos)] for i in range(nodos)]
                    
    ingresaPesos(W)
    system('cls')

    inicializaQ(W, Q)

    print('\nW')
    muestraMatriz(W)
    
    print('\nQ')
    muestraMatriz(Q)
    
    caminoMinimo(Q)

    print('\nQ')
    muestraMatriz(Q)
