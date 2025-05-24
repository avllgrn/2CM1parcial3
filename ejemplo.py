from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')
    
    mA = int(input('Dame mA '))
    nA = int(input('Dame nA '))
    
    mB = int(input('Dame mB '))
    nB = int(input('Dame nB '))
    
    if mA==mB and nA==nB:

        mC = mA
        nC = nB

        A = [ [randrange(11) for j in range(nA)] for i in range(mA)]
        B = [ [randrange(11) for j in range(nB)] for i in range(mB)]
        C = [ [0 for j in range(nC)] for i in range(mC)]

        for i in range(mC):
            for j in range(nC):
                C[i][j] = A[i][j] - B[i][j]

        print('\nA')
        for i in range(mA):
            for j in range(nA):
                print(f'{A[i][j]}', end='\t')
            print()

        print('\nB')
        for i in range(mB):
            for j in range(nB):
                print(f'{B[i][j]}', end='\t')
            print()

        print('\nA-B')
        for i in range(mC):
            for j in range(nC):
                print(f'{C[i][j]}', end='\t')
            print()
    else:
        print('Error! Las matrices no pueden restarse')

