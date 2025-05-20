from os import system

if __name__ == '__main__':
    system('cls')
    
    m = int(input('Dame m '))
    n = int(input('Dame n '))
    
    M = [ [0 for j in range(n)] for i in range(m)]
    print(M,'\n\n')

    for i in range(m):
        for j in range(n):
            print(f'{M[i][j]}', end='\t')
        print()
