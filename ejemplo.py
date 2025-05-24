from os import system
from random import randrange 

if __name__ == '__main__':
    system('cls')
    
    m = int(input('Dame m '))
    n = int(input('Dame n '))

    mT = n
    nT = m

    M = [ [randrange(11) for j in range(n)] for i in range(m)]
    MT = [ [0 for j in range(nT)] for i in range(mT)]

    for i in range(m):
        for j in range(n):
            MT[j][i] = M[i][j]

    print('\nM')
    for i in range(m):
        for j in range(n):
            print(f'{M[i][j]}', end='\t')
        print()

    print('\nMT')
    for i in range(mT):
        for j in range(nT):
            print(f'{MT[i][j]}', end='\t')
        print()
